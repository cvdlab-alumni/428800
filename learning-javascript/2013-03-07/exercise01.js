function identity(n)
{
var matrix ="";
for(var i = 1 ; i <= n ; i++)
	{
		for (var j = 1; j <= n; j++) 
		{
				i===j ? matrix+=("1"):  matrix += ("0") ;
				j!==n ? matrix+=("\t") : matrix+="";
		}
		(i!==n) ? matrix += "\n" : matrix +="";
	}
	return matrix;
}