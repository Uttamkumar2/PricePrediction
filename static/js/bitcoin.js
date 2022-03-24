
urlstring='https://group3price.herokuapp.com/readData'
//urlstring='http://127.0.0.1:5000/readData'
Plotly.d3.json(urlstring, function(err, rows){
    console.log(rows);
  console.log("java Layer " + rows)
  function unpack(rows, key) {
     return rows.map(function(row) { return row[key]; });
    }

console.log("Uttam 2");

 var open = unpack(rows, 'Open')
 var high = unpack(rows, 'High')
 var low = unpack(rows, 'Low')
 var close = unpack(rows, 'Close')
 var Volume_BTC = unpack(rows, 'Volume_(BTC)')
 var Volume_Currency =  unpack(rows, 'Volume_(Currency)') 
 var datatimes =  unpack(rows, 'Timestamp') 
 var WeightPrice = unpack(rows, 'Weighted_Price') 

var trace = {
    x: datatimes,
    y: WeightPrice,
    type: "bar"
  };

// Create the data array for the plot
var data = [trace];

// Define the plot layout
var layout = {
  title: "Weight Price vs Date & time",
  xaxis: { title: "Years" },
  yaxis: { title: "Weight Price" }
};

// Plot the chart to a div tag with id "bar-plot"
var trace1 = {
  x: datatimes,
  y: Volume_BTC,
  type: "bar"
};

// Create the data array for the plot
var data1 = [trace1];

// Define the plot layout
var layout1 = {
  title: "BTC  vs Years",
  xaxis: { title: "Years" },
  yaxis: { title: "BTC" }
};

Plotly.newPlot('plot', data, layout);
Plotly.newPlot('plot2', data1, layout1);
});
