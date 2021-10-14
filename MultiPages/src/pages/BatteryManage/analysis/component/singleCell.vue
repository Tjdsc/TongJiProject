<template>

  <div class="single-cell-com" >
    <row width="900px" style="margin-left: 0px">

      <i-col span="12">
        <h2>容量衰退曲线：</h2>
        <div id="f1" class="grid-content bg-purple" style="margin-left: 0px"></div>
      </i-col>

      <i-col span="12">
        <h2>容量跳水预测结果：</h2>
        <div id="f2" class="grid-content bg-purple"></div>
      </i-col>
    </row>

    <row >
      <i-col span="12">
        <h2>容量跳水角度评估曲线：</h2>
        <div id="f3" class="grid-content bg-purple"></div>
      </i-col>

      <i-col span="12">
        <h2>容量跳水面积评估曲线：</h2>
        <div id="f4" class="grid-content bg-purple"></div>
      </i-col>
    </row>

    <!-- <row>
      <i-col span="12">
        <h2>ICA曲线：</h2>
        <div id="ic-dv-fig" class="grid-content bg-purple"></div>
      </i-col>

      <i-col span="12">
        <h2>峰值与老化相关性：</h2>
        <div id="ic-max-fig" class="grid-content bg-purple"></div>
      </i-col>
    </row> -->

  </div>

</template>

<script>

import * as echarts from "echarts";
import axios from "axios";
import QS from "qs";


var myChart1
var myChart2
var myChart3
var myChart4
var myChart_IC_DV
var myChart_IC_DV_MAX

export default {
  name: "singleCell",
  cell_name:'',
  props: ['item'],

  data(){
    return{
      /*****************************************************/

      option1 : {
        // title:{
        //   text:'容量曲线',
        //   left:'50%'
        // },
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
        xAxis: {
          name:'循环次数',
          type: 'category',

          data: null,
          nameLocation:'center',
          nameGap:30,
          axisPointer: {
            type: 'shadow'
          }
        },

        yAxis: [{
          name:'容量/Ah',
          type: 'value',
          min: 0.8,
          max: 1.1,
          // nameLocation:'center',
          // nameGap:35,
        },{
          name: '容量保持率/%',
          type: 'value',
          min: 50,
          max: 110,
          nameLocation: 'center',
          nameGap: 30,
        },],
        legend:{
          // orient:'vertical',
          // left:0,
          top:15,
          data:["容量","容量保持率"]
        },

        series: [{
          data: null,
          type: 'line',
          symbol:'none',
          smooth: false,
          markPoint:{
            data:null,

          }
        },{
          data: null,
          type: 'line',
          symbol:'none',
          smooth: false,
          markPoint:{
            data:null,

          }
        }],

        animation:true,
      },


      option2 : {
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
        legend:{
          // orient:'vertical',
          // left:'50%',
          top:15,
          data:["预测值","真实值"]
        },
        xAxis: {
          name:'循环次数',
          type: 'category',

          data: null,
          nameLocation:'center',
          nameGap:30,
          axisPointer: {
            type: 'shadow'
          }
        },

        yAxis: {
          name:'距离跳水的循环次数',
          type: 'value',
          offset:-20,

        },
        series: [
          {
            type: 'line',
            data: null,
            smooth: true,
          },
          {
            type: 'line',
            data: null,
            smooth: true,

          }
        ],
        animation:true
      },


      option3 : {
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

        xAxis: {
          name:'循环次数',
          type: 'category',

          data: null,
          nameLocation:'center',
          nameGap:30,
          axisPointer: {
            type: 'shadow'
          }
        },
        yAxis: {
          name:'转折程度/%',
          type: 'value'
        },
        series: [{
          data: null,
          type: 'line',
          smooth: true,
          markLine: {

            symbol:"none",
            data: [
              {
                silent:false,             //鼠标悬停事件  true没有，false有
                lineStyle:{               //警戒线的样式  ，虚实  颜色
                  type:"dashed",
                  color:"red",
                  width:2,

                },
                label:{
                  position:'end',
                  formatter:"30%",


                },
                yAxis:30
              }
            ]

          },
          markPoint:{
            data:null,

          }
        }],

        animation:true
      },


      option4 : {
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

        xAxis: {
          name:'循环次数',
          type: 'category',

          data: null,
          nameLocation:'center',
          nameGap:30,
          axisPointer: {
            type: 'shadow'
          }
        },
        yAxis: {
          name:'转折程度/%',
          type: 'value'
        },
        series: [{
          data: null,
          type: 'line',
          smooth: true,
          markLine: {

            symbol:"none",
            data: [
              {
                silent:false,             //鼠标悬停事件  true没有，false有
                lineStyle:{               //警戒线的样式  ，虚实  颜色
                  type:"dashed",
                  color:"red",
                  width:2,

                },
                label:{
                  position:'end',
                  formatter:"30%",


                },
                yAxis:30
              }
            ]

          },
          markPoint:{
            data:null,

          }
        }],
        animation:true
      },

      data_IC_DV:{
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

        xAxis: {
          name:'电压/V',
          type: 'category',

          data: null,
          nameLocation:'center',
          nameGap:30,
          axisPointer: {
            type: 'shadow'
          }
        },
        yAxis: {
          name:'dQ/dV',
          type: 'value'
        },
        series: [
          {

            data: null,
            type: 'line',
            smooth: false
          }, {
            data: null,
            type: 'line',
            smooth: false
          }, {
            data: null,
            type: 'line',
            smooth: false
          }, {
            data: null,
            type: 'line',
            smooth: false
          }, {
            data: null,
            type: 'line',
            smooth: false
          }, {
            data: null,
            type: 'line',
            smooth: false
          }, {
            data: null,
            type: 'line',
            smooth: false
          }, {
            data: null,
            type: 'line',
            smooth: false
          }, {
            data: null,
            type: 'line',
            smooth: false
          }, {
            data: null,
            type: 'line',
            smooth: false
          }],
        animation:true
      },

      data_IC_DV_MAX: {
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

        xAxis: {
          name:'容量',
          type: 'category',

          data: null,
          nameLocation:'center',
          nameGap:30,
          axisPointer: {
            type: 'shadow'
          }
        },
        yAxis: {
          name:'最高峰值',
          type: 'value'
        },
        series: [{
          data: null,
          type: 'line',
          smooth: false
        }],
        animation:true
      },

    }
  },

  mounted() {

    var cell_name = this.$store.state.current_cell_name

    myChart1 = echarts.init(document.getElementById('f1'));
    myChart2 = echarts.init(document.getElementById('f2'));
    myChart3 = echarts.init(document.getElementById('f3'));
    myChart4 = echarts.init(document.getElementById('f4'));
    // myChart_IC_DV= echarts.init(document.getElementById('ic-dv-fig'));
    // myChart_IC_DV_MAX= echarts.init(document.getElementById('ic-max-fig'));

    this.$store.state.fig1_capacity = this.$store.state.all_cell_data[cell_name].capacity.capacity
    this.$store.state.fig1_cycle = this.$store.state.all_cell_data[cell_name].capacity.cycle

    for (let i in this.$store.state.fig1_cycle){
      this.$store.state.fig1_capacity_rate[i] = (this.$store.state.fig1_capacity[i]/this.$store.state.fig1_capacity[0])*100
    }
    // console.log(this.$store.state.fig1_capacity_rate)
    // console.log( this.$store.state.fig1_cycle)
    // console.log( this.$store.state.fig1_capacity)
    this.$store.state.knee_point = this.$store.state.all_cell_data[cell_name].knee_point.knee_point

    this.$store.state.normalized_capacity = this.$store.state.all_cell_data[cell_name].knee_degree.normalized_capacity
    this.$store.state.normalized_cycle = this.$store.state.all_cell_data[cell_name].capacity.normalized_cycle

    this.$store.state.angle_degree = this.$store.state.all_cell_data[cell_name].online_degree_all.angle_degree
    this.$store.state.square_degree = this.$store.state.all_cell_data[cell_name].online_degree_all.square_degree

    // console.log( this.$store.state.angle_degree)
    // console.log( this.$store.state.square_degree)
    this.$store.state.online_rank = this.$store.state.all_cell_data[cell_name].online_rank_all.online_rank

    this.$store.state.predicted_ctk = this.$store.state.all_cell_data[cell_name].predicted_ctk.predicted_ctk
    this.$store.state.true_ctk = this.$store.state.all_cell_data[cell_name].predicted_ctk.true_ctk



    // console.log(this.$store.state.all_cell_data[cellName])

    // console.log(cellName)
    this.option1.xAxis.data = this.cycle
    this.option1.series[0].name = '容量'
    this.option1.series[0].data = this.capacity
    this.option1.series[1].name = '容量保持率'
    this.option1.series[1].data = this.$store.state.fig1_capacity_rate
    this.option1.series[1].yAxisIndex = 1
    this.option1.series[0].markPoint = {
      data: [
        {
          name: '拐点',
          value: '拐点:' + this.knee_point,
          xAxis: this.knee_point,
          yAxis: this.capacity[this.knee_point],
          symbol: "pin",
          symbolSize: 50,
          symbolOffset: ['0', '0']

        }
      ]

    }
    this.option2.xAxis.data = this.cycle
    this.option2.series[0].data = this.predicted_ctk
    this.option2.series[0].name = '预测值'
    this.option2.series[1].data = this.true_ctk
    this.option2.series[1].name = '真实值'

    this.option3.xAxis.data = this.cycle
    this.option3.series[0].data = this.angle_degree
    this.option3.series[0].markPoint = {
      data: [
        {
          name: '拐点',
          value: '拐点:' + this.knee_point,
          xAxis: this.knee_point,
          yAxis: this.$store.state.angle_degree[this.knee_point],
          symbol: "pin",
          symbolSize: 50,
          symbolOffset: ['0', '0']

        }
      ]

    }

    this.option4.xAxis.data = this.cycle
    this.option4.series[0].data = this.square_degree
    this.option4.series[0].markPoint = {
      data: [
        {
          name: '拐点',
          value: '拐点:' + this.knee_point,
          xAxis: this.knee_point,
          yAxis: this.$store.state.square_degree[this.knee_point],
          symbol: "pin",
          symbolSize: 50,
          symbolOffset: ['0', '0']

        }
      ]

    }

    // this.option1.xAxis.data = this.cycle
    // this.option1.series[0].data = this.capacity
    // this.option1.series[0].name = '容量'
    // this.option1.series[1].data = this.$store.state.online_rank
    // this.option1.series[1].name = '容量保持率'
    // this.option1.series[1].yAxisIndex = 1
    // this.option1.series[0].markPoint = {
    // data: [
    //     {
    //       name: '拐点',
    //       value: '拐点:' + this.knee_point,
    //       xAxis: this.knee_point,
    //       yAxis: this.capacity[this.knee_point],
    //       symbol: "pin",
    //       symbolSize: 50,
    //       symbolOffset: ['0', '0']
    //
    //     }
    //   ]
    //
    // }
    // this.option2.xAxis.data = this.cycle
    // this.option2.series[0].data = this.predicted_ctk
    // this.option2.series[0].name = '预测值'
    // this.option2.series[1].data = this.true_ctk
    // this.option2.series[1].name = '真实值'
    //
    // this.option3.xAxis.data = this.cycle
    // this.option3.series[0].data = this.angle_degree
    // this.option3.series[0].markPoint = {
    //   data: [
    //     {
    //       name: '拐点',
    //       value: '拐点:' + this.knee_point,
    //       xAxis: this.knee_point,
    //       yAxis: this.$store.state.angle_degree[this.knee_point],
    //       symbol: "pin",
    //       symbolSize: 50,
    //       symbolOffset: ['0', '0']
    //
    //     }
    //   ]
    //
    // }
    //
    // this.option4.xAxis.data = this.cycle
    // this.option4.series[0].data = this.square_degree
    // this.option4.series[0].markPoint = {
    //   data: [
    //     {
    //       name: '拐点',
    //       value: '拐点:' + this.knee_point,
    //       xAxis: this.knee_point,
    //       yAxis: this.$store.state.square_degree[this.knee_point],
    //       symbol: "pin",
    //       symbolSize: 50,
    //       symbolOffset: ['0', '0']
    //
    //     }
    //   ]
    //
    // }



    // this.data_IC_DV.xAxis.data = this.$store.state.V_lin[0]
    // this.data_IC_DV.series[0].data = this.$store.state.IC_DV[0]
    // this.data_IC_DV.series[1].data = this.$store.state.IC_DV[1]

    // for (var i=0;i<this.$store.state.IC_DV.length;i++){
    //   this.data_IC_DV.series[i].data = this.$store.state.IC_DV[i]
    // }
    // console.log(this.$store.state.IC_DV)
    // console.log(this.data_IC_DV.series)

    // this.data_IC_DV_MAX.xAxis.data = this.$store.state.fig1_capacity
    // this.data_IC_DV_MAX.series[0].data = this.$store.state.abs_IC_DV_max
    //
    myChart1.setOption(this.option1);
    myChart2.setOption(this.option2);
    myChart3.setOption(this.option3);
    myChart4.setOption(this.option4);
    // myChart_IC_DV.setOption(this.data_IC_DV)
    // myChart_IC_DV_MAX.setOption(this.data_IC_DV_MAX)
  },

  methods: {


    test_all_cell(cellName){
      // myChart1 = echarts.init(document.getElementById('f1'));
      // myChart2 = echarts.init(document.getElementById('f2'));
      // myChart3 = echarts.init(document.getElementById('f3'));
      // myChart4 = echarts.init(document.getElementById('f4'));

      this.$store.state.fig1_capacity = this.$store.state.all_cell_data[cellName].capacity.capacity
      this.$store.state.fig1_cycle = this.$store.state.all_cell_data[cellName].capacity.cycle

      for (let i in this.$store.state.fig1_cycle){
        this.$store.state.fig1_capacity_rate[i] = (this.$store.state.fig1_capacity[i]/this.$store.state.fig1_capacity[0])*100
      }
      // console.log(this.$store.state.fig1_capacity_rate)
      // console.log( this.$store.state.fig1_cycle)
      // console.log( this.$store.state.fig1_capacity)
      this.$store.state.knee_point = this.$store.state.all_cell_data[cellName].knee_point.knee_point

      this.$store.state.normalized_capacity = this.$store.state.all_cell_data[cellName].knee_degree.normalized_capacity
      this.$store.state.normalized_cycle = this.$store.state.all_cell_data[cellName].capacity.normalized_cycle

      this.$store.state.angle_degree = this.$store.state.all_cell_data[cellName].online_degree_all.angle_degree
      this.$store.state.square_degree = this.$store.state.all_cell_data[cellName].online_degree_all.square_degree

      // console.log( this.$store.state.angle_degree)
      // console.log( this.$store.state.square_degree)
      this.$store.state.online_rank = this.$store.state.all_cell_data[cellName].online_rank_all.online_rank

      this.$store.state.predicted_ctk = this.$store.state.all_cell_data[cellName].predicted_ctk.predicted_ctk
      this.$store.state.true_ctk = this.$store.state.all_cell_data[cellName].predicted_ctk.true_ctk



      // console.log(this.$store.state.all_cell_data[cellName])

      // console.log(cellName)
      this.option1.xAxis.data = this.cycle
      this.option1.series[0].name = '容量'
      this.option1.series[0].data = this.capacity
      this.option1.series[1].name = '容量保持率'
      this.option1.series[1].data = this.$store.state.fig1_capacity_rate
      this.option1.series[1].yAxisIndex = 1
      this.option1.series[0].markPoint = {
        data: [
          {
            name: '拐点',
            value: '拐点:' + this.knee_point,
            xAxis: this.knee_point,
            yAxis: this.capacity[this.knee_point],
            symbol: "pin",
            symbolSize: 50,
            symbolOffset: ['0', '0']

          }
        ]

      }
      this.option2.xAxis.data = this.cycle
      this.option2.series[0].data = this.predicted_ctk
      this.option2.series[0].name = '预测值'
      this.option2.series[1].data = this.true_ctk
      this.option2.series[1].name = '真实值'

      this.option3.xAxis.data = this.cycle
      this.option3.series[0].data = this.angle_degree
      this.option3.series[0].markPoint = {
        data: [
          {
            name: '拐点',
            value: '拐点:' + this.knee_point,
            xAxis: this.knee_point,
            yAxis: this.$store.state.angle_degree[this.knee_point],
            symbol: "pin",
            symbolSize: 50,
            symbolOffset: ['0', '0']

          }
        ]

      }

      this.option4.xAxis.data = this.cycle
      this.option4.series[0].data = this.square_degree
      this.option4.series[0].markPoint = {
        data: [
          {
            name: '拐点',
            value: '拐点:' + this.knee_point,
            xAxis: this.knee_point,
            yAxis: this.$store.state.square_degree[this.knee_point],
            symbol: "pin",
            symbolSize: 50,
            symbolOffset: ['0', '0']

          }
        ]

      }

      myChart1.setOption(this.option1);
      myChart2.setOption(this.option2);
      myChart3.setOption(this.option3);
      myChart4.setOption(this.option4);
    //
    //   myChart1.setOption();
    //   myChart2.setOption();
    //   myChart3.setOption();
    //   myChart4.setOption();
    },

    get_Cell_Data(item) {
      this.getCapacity(item)
      // this.getKnee_Point(item)
      // this.getPredicted_ctk(item)
      // this.getKnee_degree(item)
      // this.getOnline_degree_all(name)
      // this.getOnline_rank_all(name)




    },

    getCapacity(name) {
      axios.post(this.$store.state.http_header + this.$store.state.ip + this.$store.state.route_capacity, QS.stringify({
        name: name,
        project_id: 0,
      })).then(response => {
        console.log(response);
        this.$store.state.fig1_capacity = response.data.capacity;
        this.$store.state.fig1_cycle = response.data.cycle;
      })


    },

    getKnee_Point(name) {
      axios.post(this.$store.state.http_header + this.$store.state.ip + this.$store.state.route_knee_point, QS.stringify({
        name: name,
        project_id: 0,

      })).then(response => {
        console.log(response);
        this.$store.state.knee_point = response.data.knee_point;
      })
    },

    getKnee_degree(name) {
      axios.post(this.$store.state.http_header + this.$store.state.ip + this.$store.state.route_knee_degree, QS.stringify({
        name: name,
        project_id: 0,

      })).then(response => {
        console.log(response);
        this.$store.state.angle_method = response.data.angle_method;
        this.$store.state.square_method = response.data.square_method;
      })
    },

    getOnline_degree_all(name) {
      axios.post(this.$store.state.http_header + this.$store.state.ip + this.$store.state.route_online_degree_all, QS.stringify({
        name: name,
        project_id: 0,

      })).then(response => {
        console.log(response);
        this.$store.state.online_degree = response.data.online_degree;
        this.$store.state.valid_length = response.data.valid_length;
      })
    },

    getOnline_rank_all(name) {
      axios.post(this.$store.state.http_header + this.$store.state.ip + this.$store.state.route_online_rank_all, QS.stringify({
        name: name,
        project_id: 0,

      })).then(response => {
        console.log(response);
        this.$store.state.online_rank = response.data.online_rank;
        this.$store.state.diff_cycle = response.data.diff_cycle;
      })
    },

    getPredicted_ctk(name) {
      axios.post(this.$store.state.http_header + this.$store.state.ip + this.$store.state.route_predicted_ctk, QS.stringify({
        name: name,
        project_id: 0,

      })).then(response => {
        console.log(response);
        this.$store.state.predicted_ctk = response.data.predicted_ctk;
        this.$store.state.true_ctk = response.data.true_ctk;
      })
    },

  },

  created() {
    // this.test_all_cell()
    // this.item = 'ccc'

  },
  watch: {

    //
    // 'current_cell_name': {
    //   immediate: true,
    //   deep: true,
    //   handler(newVal, oldVal) {
    //     console.log(newVal);
    //     console.log(oldVal);
    //
    //     // this.get_Cell_Data(newVal)
    //
    //     this.test_all_cell(newVal)
    //
    //
    //   },
    // },

    item: {

      handler(newVal, oldVal) {
        console.log(newVal);
        console.log(oldVal);

        // this.get_Cell_Data(newVal)

        this.test_all_cell(newVal)


      },

      // immediate: true,
      // deep:true,
    },



    // params:{
    //
    //   item:function (newVal,oldVal) {
    //     console.log(newVal);
    //     console.log(oldVal);
    //
    //     // this.get_Cell_Data(newVal)
    //
    //     this.test_all_cell(newVal)
    //   },
    //
    //   deep:true,
    //
    // },
    //
    // property:{
    //   immediate:true,
    //
    //   item:function (newVal,oldVal) {
    //     console.log(newVal);
    //     console.log(oldVal);
    //
    //     // this.get_Cell_Data(newVal)
    //
    //     this.test_all_cell(newVal)
    //   }
    // },



  },

  computed: {

    capacity() {
        return this.$store.state.fig1_capacity
      },
    cycle() {
        return this.$store.state.fig1_cycle
      },
    knee_point() {
        return this.$store.state.knee_point
      },
    predicted_ctk() {
        return this.$store.state.predicted_ctk
      },
    true_ctk() {
        return this.$store.state.true_ctk
      },
    angle_degree() {
        return this.$store.state.angle_degree
      },
    square_degree() {
        return this.$store.state.square_degree
      },

    current_cell_name(){

      return this.$store.state.current_cell_name

    }

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
