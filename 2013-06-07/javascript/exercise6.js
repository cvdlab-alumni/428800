function stampaLar(modelloLAR){

	var V = modelloLAR[0];

	var FV = modelloLAR[1];

	var result = "";

	for (var i = 0; i < V.length; i++){

		result+= "V: ";

		if(V[i][2] !== undefined)
			result+= V[i][0]+" "+V[i][1]+" "+V[i][2] : result+= V[i][0]+" "+V[i][1]+" 0"

		result+="\n";

	}

	result+="\n";

	for (var i = 0; i < FV.length; i++){

		result+="FV: ";

		for (var j = 0; j < FV[i].length; j++) {

			result+=FV[i][j] + " ";

		};

		result+="\n";
	}
	
	return result;
}