import sys
import codecs
f = codecs.open('out.out', encoding='utf-8', mode='w+')
sys.stdout = f
import xml.etree.ElementTree as ET
from prettyDesc import prettyDesc

def prettyDesc(description):
    #do some work before converting to html
    description = html2text(description)
    #do somework afterwards
    return description

datosDeInteres = [	
		"FormattedID", # ID en el Rally
		"Name", # titulo
		"Description", # descripcion && criterios de aceptacion
		
		"PlanEstimate",# story points
		"Owner.refObjectName",# story owner
		"Iteration.refObjectName",# iteracion
		"ScheduleState" # estado
		# tambien levanta "Tasks" = [titulosDeSusTasks]
	]
stories = []
actual = -1
def rellenar (root, padre = None):
	global actual
	global stories
	actual+=1
	stories.append({})
	
	hijos = []
	for child in root:
		for dato in datosDeInteres:
			if dato.find(".") != -1:
				tag = dato[:dato.find(".")]
				attrib = dato[dato.find(".")+1:]
				if child.tag == tag:
					stories[actual][tag] = child.attrib[attrib]
			else:
				tag = dato
				if child.tag == tag:
					if child.text:
						stories[actual][tag] = child.text
					else:
						stories[actual][tag] = ""
		if child.tag == "Tasks":
			stories[actual]["Tasks"] = []
			for t in child:
				stories[actual]["Tasks"].append(t.attrib["refObjectName"])
				
		if child.tag == "HierarchicalRequirement":
			rellenar(child)
		if child.tag == "Children":
			hijos.append(child)
	if stories[actual] != {} and padre:
		stories[actual]["Padre"] = padre
	for h in hijos:
		rellenar(h, actual)

tree = ET.parse('stories.xml')
rellenar(tree.getroot())
maxdig = 1000000

def imprimirTask(s):

	print "\t\\task"+"\t{" + s["FormattedID"]+ "} % ID en el Rally"
	print "\t\t{" + s["Name"] + "} % titulo"
	print "\t\t{" + prettyDesc(s["Description"]) + "} % descripcion"

	if s.get("Estimate"):
		print "\t\t{" + s["Estimate"] + "} % horas estimadas"
	else:
		print "\t\t{" + "} % horas estimadas"
	if s.get("Owner"):	
		print "\t\t{" + s["Owner"] + "} % story owner"
	else:
		print "\t\t{" + "} % story owner"
	if s.get("ToDo"):
		print "\t\t{" + s["ToDo"] + "} % horas faltantes"
	else:
		print "\t\t{" + "} % horas faltantes"
	print "\t\t{" + s["State"]+ "} % estado (completada, bloqueada, etc.)"
	print


datosDeInteres = [	
		"FormattedID",#{TA35} % ID en el Rally
		"Name",#titulo
		"Description",# descripcion
		"Estimate",#{4} % horas estimadas
		"Owner.refObjectName",#{Ivan P} % responsable
		"ToDo",#{0} % horas faltantes
		"State"#{Completada} % estado (completada, bloqueada, etc.)
	]
tasks = []
actual = -1
def rellenar2 (root, padre = None):
	global actual
	global stories
	actual+=1
	tasks.append({})
	for child in root:
		for dato in datosDeInteres:
			if dato.find(".") != -1:
				tag = dato[:dato.find(".")]
				attrib = dato[dato.find(".")+1:]
				if child.tag == tag:
					tasks[actual][tag] = child.attrib[attrib]
			else:
				tag = dato
				if child.tag == tag:
					if child.text:
						tasks[actual][tag] = child.text
					else:
						tasks[actual][tag] = ""
		if child.tag == "Tasks":
			tasks[actual]["Tasks"] = []
			for t in child:
				tasks[actual]["Tasks"].append(t.attrib["refObjectName"])
				
		if child.tag == "HierarchicalRequirement" or child.tag == "Task":
			rellenar2(child)


tree = ET.parse('tasks.xml')
rellenar2(tree.getroot())
for s in stories:
	if s == {}:
		continue
	print "\userStory" + "\t{" + s["FormattedID"]+ "} % ID en el Rally"

	print "\t{" + s["Name"] + "} % titulo"
	print "\t{" + prettyDesc(s["Description"]) + "} % descripcion"
	if s.has_key("Criterios"):
		print "\t{" + s["Criterios"] + "} % criterios de aceptacion"
	else:
		print "\t{" + "} % criterios de aceptacion"
	
	if s.get("PlanEstimate"):
		print "\t{" + s["PlanEstimate"] + "} % story points"
	else:
		print "\t{" + "} % story points"
	print "\t{" + s["Owner"] + "} % story owner"
	if s.get("Iteration") == "1":
		print "\t{" + "Primera"+ "} % iteracion (Primera o ``no definida'')"
	else:
		print "\t{" + "no definida"+ "} % iteracion (Primera o ``no definida'')"
	print "\t{" + s["ScheduleState"]+ "} % estado (completada, bloqueada, etc.)"
	print
	for t in s["Tasks"]:
		for tt in tasks:
			if t == tt.get("Name"):
				imprimirTask(tt)
	print
	print "\\vspace{20pt}"
	print


