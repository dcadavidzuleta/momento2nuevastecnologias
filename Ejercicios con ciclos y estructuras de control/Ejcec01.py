calificaciones = {'Español': 3, 'Matematicas': 5, 'Ingles': 2, 'Fisica': 4}

nombresMaterias = tuple(calificaciones.keys())
notasMaterias = tuple(calificaciones.values())
notaAlta = nombresMaterias[notasMaterias.index(max(notasMaterias))]
print('La materia con la nota más alta es ', notaAlta)