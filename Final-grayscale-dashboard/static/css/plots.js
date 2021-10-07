console.log(data);

names = data.map(function (row){
    return row.state_name
  });
  
  // Trace for the Greek Data
  let trace1 = {
      x: data.map(row => row.state_name),
      y: data.map(row => row.change),
      type: "bar"
    };
  
  // Data trace array
  let traceData = [trace1];
  
  // Apply the group barmode to the layout
  let layout = {
    title: "Population from 2010 to 2020"
  };
  
  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("plot", traceData, layout);
  