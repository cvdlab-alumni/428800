var matrix = "" ;
for(var i = 1 ; i <= 100 ; i++)
	{
		(i%10===0) ? matrix+=(i + "\n") : matrix += (i + ",\t");
	}
console.log(matrix);
