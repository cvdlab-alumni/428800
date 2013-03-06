var matrix = "" ;
for(var i = 1 ; i <= 10 ; i++)
	{
		for (var j = 1; j <= 10; j++) 
		{
				i===j ? matrix+=("1" + "\t" ): matrix += ("0" + "\t");
		}
		matrix += "\n";
	}
console.log(matrix);
 