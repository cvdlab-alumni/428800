var data = [
  {id:'01', name:'duffy'},
  {id:'02', name:'michey'},
  {id:'03', name:'donald'},
  {id:'04', name:'goofy'},
  {id:'05', name:'minnie'},
  {id:'06', name:'scrooge'}
];
var key = 'name';
var values = ['goofy', 'scrooge'];

function select (data, key, values)
{
	var selection = [];
	for( var i = 0 ; i < data.length ; i ++ )
	{
		if(values.some(function(item, index, array) {return data[i][key]===item} ))  
		{
			selection.push(data[i]);
		}
	}
	return selection;
}