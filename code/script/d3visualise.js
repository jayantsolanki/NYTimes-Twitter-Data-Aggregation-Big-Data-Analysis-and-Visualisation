var wordCount = [];
    var fontSizeScale = d3.scale.pow().exponent(5).domain([0,1]).range([10, 60]);
    var color = d3.scale.category10();
    var divSelect = ''
    var numRows = 0;
       // var color = d3.scale.linear()
       //      .domain([0,1,2,3,4,5,6,10,15,20,100])
       //      .range(["#ddd", "#ccc", "#bbb", "#aaa", "#999", "#888", "#777", "#666", "#555", "#444", "#333", "#222"]);
      $(document).ready(function(){
        
          $("#button1").click(function(){//nytimes single
            wordCount = [];
            var optionSelected = $("#nytimessingle").find(":selected").val();
            numRows = $("#nytimessingleCount").val();
            divSelect = "#cloud1";
            // alert(numRows)
            // alert(optionSelected)
              $.ajax({
                url: 'nytimes/'+optionSelected+'.csv',
                dataType: 'text',
              }).done(createJSONarray);
          });
          $("#button2").click(function(){//twitter single
            wordCount = [];
            var optionSelected = $("#twitsingle").find(":selected").val();
            numRows = $("#twitsingleCount").val();
            divSelect = "#cloud2";
            // alert(numRows)
            // alert(optionSelected)
              $.ajax({
                url: 'twitter/'+optionSelected+'.csv',
                dataType: 'text',
              }).done(createJSONarray);
          });
          $("#button3").click(function(){//nytimes co-occurrence
            wordCount = [];
            var optionSelected = $("#nytimesco").find(":selected").val();
            numRows = $("#nytimescoCount").val();
            divSelect = "#cloud3";
            // alert(numRows)
            // alert(optionSelected)
              $.ajax({
                url: 'nytimes/'+optionSelected+'co.csv',
                dataType: 'text',
              }).done(createJSONarray);
          });
          $("#button4").click(function(){// twitter co-occerrence
            wordCount = [];
            var optionSelected = $("#twitco").find(":selected").val();
            numRows = $("#twitcoCount").val();
            divSelect = "#cloud4";
            // alert(numRows)
            // alert(optionSelected)
              $.ajax({
                url: 'twitter/'+optionSelected+'co.csv',
                dataType: 'text',
              }).done(createJSONarray);
          });
      });
      function createJSONarray(data) {

        var allRows = data.split(/\r?\n|\r/);
        // var table = '<table>';
        for (var numRow = 0; numRow < allRows.length; numRow++) {
          wc = {}
          var rowCells = allRows[numRow].split(',');
          for (var rowCell = 0; rowCell < 2; rowCell++) {
            if (numRow === 0) {//plot the column names
            } else {
              if(rowCell==0)
                if(rowCells[rowCell].trim() == '')// donot want to have blanks
                  continue;
                else
                  wc['text'] = rowCells[rowCell];
              else
                if(rowCells[0] == '')// donot want to have blanks
                  continue;
                else
                  wc['size'] = parseInt(rowCells[rowCell]);
            }
          }
          if(wc.length!=0 && numRow!=0)
          {
            wordCount.push(wc)
            // console.log(wc)
          }

        } 
        wordCount.sort(function(a,b) { return parseFloat(b.size) - parseFloat(a.size) } ); 
        wordCount = wordCount.slice(0,numRows)
        calculateCloud(wordCount)
      }
      function JSONsort(data){// very crude selection sort
        sortedWordCount = [] 
        count = 0
        for(var item = 0; item< data.length-1; item++){
          var temp = {}
          var key = item

          for(var it = item+1; it< data.length; it++){
            if(data[it].size >= data[key].size)
            {

              key = it

            }
          }
          count = count+1
          temp= data[item]
          data[item] = data[key]
          data[key] = temp
          // sortedWordCount.push(data[key])
          if(count == 20)
            break

        }
        wordCount = data.slice(0,20)
        // calculateCloud(wordCount)

      }
      

    function calculateCloud(data) {
      var maxVal = data[0].size
      console.log(data)
      d3.layout.cloud().size([1000, 400])
              .words(data)
              .rotate(0)
              .fontSize(function(d) { return fontSizeScale(d.size/maxVal) })
              .on("end", draw)
              .start();
    }

    function draw(words) {

      // console.log(words)
      $(divSelect).empty();
        d3.select(divSelect).append("svg")
                .attr("width", 950)
                .attr("height", 450)
                .attr("class", "wordcloud")
                .append("g")
                // without the transform, words would get cutoff to the left and top, they would
                // appear outside of the SVG area
                .attr("transform", "translate(320,200)")
                .selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", function(d) { return d.size + "px"; })
                .style("fill", function(d, i) { return color(i); })
                .attr("transform", function(d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .attr('text-anchor', 'middle')
                .text(function(d) { return d.text; });
    }


      // function calculateCloud(data) {
      //   // 
      //   d3.layout.cloud()
      //     .size([600, 400])
      //     .words(data) // data from PubNub
      //     .rotate(function() { return ~~(Math.random()*2) * 90;}) // 0 or 90deg
      //     .fontSize(function(d) { return fontSizeScale(d.size/1400) })
      //     .on('end', drawCloud)
      //     .start();
      // }
      // function drawCloud(words) {
      //   console.log(words)
      //   // console.log(maxSize)
      //   var colors = d3.scale.category10();
      //   d3.select('#cloud').append('svg')
      //     .attr('width', 600).attr('height', 400)
      //     .append('g')
      //     .selectAll('text')
      //     .data(words)
      //     .enter().append('text')
      //     .style("font-size", function(d) { return Math.min(2 * 10, (2 * 10 - 8) / this.getComputedTextLength() * 24) + "px"; })
      //     .style('font-family', function(d) { return d.font; })
      //     .style('fill', function(d, i) { return colors(i); })
      //     .attr('text-anchor', 'middle')
      //     .attr('transform', function(d) {
      //       return 'translate(' + [d.x, d.y] + ')rotate(' + d.rotate + ')';
      //     })
      //     .text(function(d) { return d.text; });

      // }
//       function zoomToFitBounds() {

//       var X0 = d3.min( words, function (d) {
//         return d.x - (d.width/2);
//       }),
//         X1 = d3.max( words, function (d) {
//           return d.x + (d.width/2);
//         });

//       var Y0 = d3.min( words, function (d) {
//           return d.y - (d.height/2);
//         }),
//         Y1 = d3.max( words, function (d) {
//           return d.y + (d.height/2);
//         });

//       var scaleX = (X1 - X0) / (width);
//       var scaleY = (Y1 - Y0) / (height);

//       var scale = 1 / Math.max(scaleX, scaleY);

//       var translateX = Math.abs(X0) * scale;
//       var translateY = Math.abs(Y0) * scale;

//       cloud.attr("transform", "translate(" +
//         translateX + "," + translateY + ")" +
//         " scale(" + scale + ")");
// }