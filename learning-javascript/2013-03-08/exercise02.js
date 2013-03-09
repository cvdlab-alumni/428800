function generateArrayRandom(n)
{
var randoms = [];
	for (i = 0 ; i < n ; i++)
	{
		randoms.push(Math.floor(Math.random()*10));
	}
	return randoms;
}

function filterEven(item)
{
		return item % 2 === 0
}

var array = generateArrayRandom(11).filter(filterEven).sort();