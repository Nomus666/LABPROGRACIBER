#Practica3
#Registro Gym para su rutina mensual 
echo "Ingrese su nombre"
read nom

echo "Bienvenido,$nom"

#Parametros

#Funcion a usar 
rutina(){
	echo "Cual es tu meta en el gym. 1- Definicion. 2- Masa muscular. 3-Mantenimiento"

	read mot

	ej1="Series 4x12 reps\n Brazo(Bicep/Tricep)"
	ej2="Series 4x12 reps\n Torso(Pecho/Espalda"
	ej3="Series 4x12 reps\n Pierna(Cuadricep/Femorales)"

	if [ $mot -eq 1 ]; #Estructura de control
		then

			echo "Tu meta sera Definicion. Tu Rutina sera:, $ej1"

	elif [ $mot -eq 2 ];
		then
			echo "Tu meta sera Aumento de Masa. Tu Rutina sera:, $ej2"

	elif [ $mot -eq 3 ];
		then
			echo "Tu meta sera Resistencia. Tu Rutina sera:, $ej3"
	else
		echo "Numero invalido"
	fi
echo "Exito en tu rutina!"
}

rutina
