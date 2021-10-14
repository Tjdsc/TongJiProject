<template>

  <div class="all-cell-com" style="margin-top: 50px">
    <row width="900px">
      <i-col span="24">
        <h2>所有电池容量衰退曲线：</h2>
        <div id="all-cell-capacity" class="grid-content bg-purple" style="margin-top: 100px"></div>
      </i-col>
    </row>

    <row width="900px" v-show="false">
      <i-col span="24">
        <h2 style="margin-top: 50px" >所有电池当前容量与老化程度：</h2>
        <div id="all-cell-degradation" class="grid-content bg-purple" style="margin-top: 100px"></div>
      </i-col>
    </row>

    <row width="900px">
      <i-col span="18">
        <h2 style="margin-top: 50px">电池老化评估及危险等级：</h2>
        <div id="all-cell-evaluation" class="grid-content bg-purple" style="margin-top: 50px"></div>
      </i-col>

      <i-col span="6">
      <h2 style="margin-top: 50px"></h2>
      <div id="all-cell-evaluation-explain" class="grid-content bg-purple" style="max-resolution: res;        gin-top: 50px"></div>
    </i-col>
    </row>
  </div>
</template>

<script>

import * as echarts from "echarts";


var myChart_all_cell_capacity
var myChart_all_cell_degradation
var myChart_all_cell_evaluation
var myChart_all_cell_evaluation_explain

var aging_cycles =[0,400,600,800,1000,1200,1400,1600,1800]

export default {
  name: "allCell",

  data(){
    return{
      option_all_cell_capacity : {

        title:{
          text:'容量衰减曲线',
          left:'50%'
        },

        tooltip:{
          trigger:"axis",
          confine:true,
          position:['100%','100%'],
          axisPointer: {
            type: 'cross',
            crossStyle: {
              color: '#999'
            }
          },
        },

        toolbox:{
          feature: {
            dataView: {show: true, readOnly: false},
            dataZoom: {
              yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
          }
        },


        legend:{
          orient:'vertical',
          left:0,
          top:15,
          data:["b1c4","b1c20", "b1c21","b1c23", "b1c26","b1c40", "b1c41","b1c44", "b2c4","b2c21",
            "b2c22",
            "b2c24",
            "b2c31",
            "b2c39",
            "b2c45",
            "b3c8",
            "b3c10",
            "b3c13",
            "b3c15",
            "b3c20",
            "b3c30",
            "b3c31",
            "b3c36",
            "b3c43",
            "b3c45"]
        },

        grid:[{
          left:'30%'
        }],

        xAxis: {
          name:'循环圈数',
          type: 'category',
          // axisLabel:{interval:99,},
          data: null,
          nameLocation:'center',
          nameGap:30,
          // boundaryGap:false,
        },
        yAxis: {
          name:'容量/Ah',
          type: 'value',
          min: 0.8,
          max: 1.1,
          nameLocation:'center',
          nameGap:40,
        },
        series: [{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },],
        animation:true
      },

      option_all_cell_degradation : {

        title:{
          text:'当前容量值与老化程度',
          left:'50%'
        },

        tooltip:{
          trigger:"axis",
          confine:true,
          position:['100%','100%'],
          axisPointer: {
            type: 'cross',
            crossStyle: {
              color: '#999'
            }
          },
        },

        toolbox:{
          feature: {
            dataView: {show: true, readOnly: false},
            dataZoom: {
              yAxisIndex: 'none'
            },
            magicType: {show: true, type: ['line', 'bar']},
            restore: {},
            saveAsImage: {}
          }
        },


        legend:{
          orient:'vertical',
          left:0,
          top:15,
          data:["当前容量","老化程度"]
        },

        grid:[{
          left:'30%'
        }],

        xAxis: {
          name:'电池名称',
          type: 'category',
          axisLabel:{
            interval:0,
            rotate:90,
          },
          data: null,
          nameLocation:'center',
          nameGap:60,
          axisPointer: {
            type: 'shadow'
          }

          // boundaryGap:false,
        },
        yAxis: [{
          name: '当前容量/Ah',
          type: 'value',
          min: 0.87,
          // max: 1.1,
          nameLocation: 'center',
          nameGap: 50,
        }, {
          name: '老化程度/Ah',
          type: 'value',
          min: 15,
          max: 20,
          nameLocation: 'center',
          nameGap: 40,
        },],
        series: [{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },{
          data: null,
          type: 'line',
          smooth: true
        },],
        animation:true
      },

      option_all_cell_evaluation : {
        tooltip: {
          position: 'top'
        },
        grid: {
          height: '50%',
          top: '10%'

        },
        xAxis: {
          name:'电池名称',
          type: 'category',
          data: null,
          axisLabel:{
            interval:0,
            rotate:90,
          },
          splitArea: {
            show: true
          },
          nameLocation:'center',
          nameGap:60,
        },
        yAxis: {
          name:'循环数',
          type: 'category',
          data: null,
          splitArea: {
            show: true
          },
          nameLocation:'center',
          nameGap:40,
        },
        visualMap: {
          min: 0,
          max: 8,
          calculable: true,
          orient: 'horizontal',
          left: 'center',
          bottom: '5%'
        },
        series: [{
          name: 'Punch Card',
          type: 'heatmap',
          data: null,
          label: {
            show: true
          },
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          }
        }]
      },

      option_all_cell_evaluation_explain : {
        tooltip: {
          position: 'top'
        },
        grid: {
          height: '30%',
          width:'30%',
          top: '50%'
        },
        xAxis: {
          name:'跳水程度',
          type: 'category',
          data: ['慢','中','快'],
          axisLabel:{
            interval:0,
            rotate:0,
          },
          splitArea: {
            show: true
          },
          // nameLocation:'center',
          nameGap:20,
        },
        yAxis: {
          name:'剩余寿命',
          type: 'category',
          data: ['长','中','短'],
          splitArea: {
            show: true
          },
          // nameLocation:'center',
          // nameGap:60,
        },
        visualMap: {
          min: 0,
          max: 8,
          calculable: true,
          orient: 'horizontal',
          left: 'center',
          bottom: '5%',
          show:false,
        },
        series: [{
          name: 'Punch Card',
          type: 'heatmap',
          data: [[0,0,0],[1,0,1],[2,0,3],[0,1,2],[1,1,4],[2,1,6],[0,2,5],[1,2,7],[2,2,8]],
          label: {
            show: true
          },
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          }
        }]
      }

    }
  },

  mounted() {

    var cells = 0

    myChart_all_cell_capacity = echarts.init(document.getElementById('all-cell-capacity'));
    myChart_all_cell_degradation = echarts.init(document.getElementById('all-cell-degradation'));
    myChart_all_cell_evaluation = echarts.init(document.getElementById('all-cell-evaluation'));
    myChart_all_cell_evaluation_explain = echarts.init(document.getElementById('all-cell-evaluation-explain'));
    /***************************调试语句*****************/


    this.$store.state.b1c4 = this.$store.state.all_cell_data.b1c4
    this.option_all_cell_capacity.xAxis.data = this.$store.state.b1c4.capacity.cycle
    // this.option_all_cell_capacity.series[0].data = this.$store.state.fig1_cycle
    for (var i=0;i<this.$store.state.cell_name_list.length;i++){
      this.option_all_cell_capacity.series[i].data = this.$store.state.all_cell_data[this.$store.state.cell_name_list[i]].capacity.capacity
      this.option_all_cell_capacity.series[i].name = this.$store.state.cell_name_list[i]
    }


    this.option_all_cell_degradation.xAxis.data = this.$store.state.cell_name_list

    this.option_all_cell_degradation.series[0].name = '当前容量'
    this.option_all_cell_degradation.series[0].type = 'line'
    this.option_all_cell_degradation.series[0].data = this.$store.state.current_capacity
    this.option_all_cell_degradation.series[0].smooth = false

    this.option_all_cell_degradation.series[1].name = '老化程度'
    this.option_all_cell_degradation.series[1].type = 'bar'
    this.option_all_cell_degradation.series[1].data = this.$store.state.aging_degree
    this.option_all_cell_degradation.series[1].yAxisIndex = 1


    //这个老化评估图，x轴为电池数，y轴为每隔200圈的老化程度变化；

    this.option_all_cell_evaluation.xAxis.data = this.$store.state.cell_name_list
    this.option_all_cell_evaluation.yAxis.data = aging_cycles

    for (var c= 0;c<this.$store.state.cell_name_list.length;c++){
      // console.log(cell)
      var cell = this.$store.state.cell_name_list[c]

      var singleCell = this.$store.state.all_cell_data[cell]

      var square_aging = singleCell.online_degree_all.square_degree
      var cell_aging_rate = []

      for (let cycle in singleCell.capacity.cycle){
        cell_aging_rate[cycle] = (singleCell.capacity.capacity[cycle]/singleCell.capacity.capacity[0])*100
      }



      for (i = 0;i<aging_cycles.length;i++){

        var cycles = singleCell.capacity.cycle.length

        if (aging_cycles[i]<cycles){

          if (cell_aging_rate[aging_cycles[i]]>=98){
            this.$store.state.all_cell_evaluation.push([cells,i,0])
          }else if (cell_aging_rate[aging_cycles[i]]>=90){

            if (square_aging[aging_cycles[i]]<20){
              this.$store.state.all_cell_evaluation.push([cells,i,0])
            }else if (square_aging[aging_cycles[i]]<35){
              this.$store.state.all_cell_evaluation.push([cells,i,1])
            }else {
              this.$store.state.all_cell_evaluation.push([cells,i,3])
            }


          }else if (cell_aging_rate[aging_cycles[i]]>=85){

            if (square_aging[aging_cycles[i]]<20){
              this.$store.state.all_cell_evaluation.push([cells,i,2])
            }else if (square_aging[aging_cycles[i]]<35){
              this.$store.state.all_cell_evaluation.push([cells,i,4])
            }else {
              this.$store.state.all_cell_evaluation.push([cells,i,6])
            }

          }else {

            if (square_aging[aging_cycles[i]]<20){
              this.$store.state.all_cell_evaluation.push([cells,i,5])
            }else if (square_aging[aging_cycles[i]]<35){
              this.$store.state.all_cell_evaluation.push([cells,i,7])
            }else {
              this.$store.state.all_cell_evaluation.push([cells,i,8])
            }

          }
        } else {


          if (cell_aging_rate[cycles-1]>=98){
            this.$store.state.all_cell_evaluation.push([cells,i,0])
          }else if (cell_aging_rate[cycles-1]>=90){

            if (square_aging[cycles-1]<20){
              this.$store.state.all_cell_evaluation.push([cells,i,0])
            }else if (square_aging[cycles-1]<35){
              this.$store.state.all_cell_evaluation.push([cells,i,1])
            }else {
              this.$store.state.all_cell_evaluation.push([cells,i,3])
            }


          }else if (cell_aging_rate[cycles-1]>=85){

            if (square_aging[cycles-1]<20){
              this.$store.state.all_cell_evaluation.push([cells,i,2])
            }else if (square_aging[cycles-1]<35){
              this.$store.state.all_cell_evaluation.push([cells,i,4])
            }else {
              this.$store.state.all_cell_evaluation.push([cells,i,6])
            }

          }else {

            if (square_aging[cycles-1]<20){
              this.$store.state.all_cell_evaluation.push([cells,i,5])
            }else if (square_aging[cycles-1]<35){
              this.$store.state.all_cell_evaluation.push([cells,i,7])
            }else {
              this.$store.state.all_cell_evaluation.push([cells,i,8])
            }

          }

          break;

        }

      }

      cells=cells+1

    }
    this.option_all_cell_evaluation.series[0].data = this.$store.state.all_cell_evaluation



    //老化评估解释图




    // console.log(this.$store.state.all_cell_evaluation)

    myChart_all_cell_degradation.setOption(this.option_all_cell_degradation)
    myChart_all_cell_capacity.setOption(this.option_all_cell_capacity)
    myChart_all_cell_evaluation.setOption(this.option_all_cell_evaluation)
    myChart_all_cell_evaluation_explain.setOption(this.option_all_cell_evaluation_explain)
    },

  methods:{
    get_ALL_Data(){



      myChart_all_cell_capacity.setOption(this.option_all_cell_capacity)
    },
  },

}
</script>

<style scoped>
.bg-purple {
  background: white;
}
.grid-content {
  border-radius: 4px;
  min-height: 320px;
  min-width: 320px;
}
</style>
