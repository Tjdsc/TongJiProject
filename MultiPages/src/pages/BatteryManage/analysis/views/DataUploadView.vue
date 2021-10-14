
<template>
  <div id="DataUpload" >
    <template>
      <i-form :model="formItem" :label-width="80" :style="{width: '900px', padding: '50px 150px'}">
        <h2>请输入电池信息并上传数据：</h2>
        <br>

        <RadioGroup v-model="border" :style="{padding: '10px 20px'}">
          <h3>电池材料体系：</h3>
          <br>
          <Radio label="NCA" border></Radio>
          <Radio label="NCM" border></Radio>
          <Radio label="磷酸铁锂" border></Radio>
          <Radio label="钴酸锂" border></Radio>
          <Radio label="其他体系" border></Radio>
        </RadioGroup>

        <br>

        <h3 :style="{padding: '10px 20px'}">老化评估预警阈值定义：</h3>

        <div :style="{padding: '10px 20px'}"> 第一预警阈值：</div><Input v-model="value" placeholder="推荐填写：90" style="width: 300px" :style="{padding: '5px 20px'}"/>
        <div :style="{padding: '10px 20px'}"> 第二预警阈值：</div><Input v-model="value" placeholder="推荐填写：85" style="width: 300px" :style="{padding: '5px 20px'}"/>
        <br>
        <h3 :style="{padding: '10px 20px'}">目标老化区间：</h3>
        <div class="block" :style="{padding: '10px 20px'}">
          <el-slider
              v-model="agingvalue"
              range
              :marks="marks">
          </el-slider>
        </div>


<!--        <form-item label="电池类型">-->
<!--          <el-select v-model="cell_type_value" placeholder="请选择">-->
<!--            <el-option-->
<!--                v-for="item in cell_type_options"-->
<!--                :key="item.cell_type_value"-->
<!--                :label="item.cell_type_label"-->
<!--                :value="item.cell_type_value">-->
<!--            </el-option>-->
<!--          </el-select>-->
<!--        </form-item>-->
        <br>
<!--        <form-item label="预警阈值选择：">-->

<!--          <el-select v-model="cell_type_value" placeholder="请选择">-->
<!--            <el-option-->
<!--                v-for="item in cell_type_options"-->
<!--                :key="item.cell_type_value"-->
<!--                :label="item.cell_type_label"-->
<!--                :value="item.cell_type_value">-->
<!--            </el-option>-->
<!--          </el-select>-->
<!--        </form-item>-->
<!--        <form-item label="老化区间">-->

<!--          <el-select v-model="cell_type_value" placeholder="请选择">-->
<!--            <el-option-->
<!--                v-for="item in cell_type_options"-->
<!--                :key="item.cell_type_value"-->
<!--                :label="item.cell_type_label"-->
<!--                :value="item.cell_type_value">-->
<!--            </el-option>-->
<!--          </el-select>-->

<!--        </form-item>-->
        <h3 :style="{padding: '10px 20px'}">文件上传：</h3>
        <form-item label="">
          <el-upload
            class="upload-demo"
            drag
            action="http://100.68.246.17:5000/DataUploadView"
            multiple>
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">*只能上传jpg/png文件，且不超过500kb</div>
        </el-upload>
        </form-item>

        <form-item>
          <el-button @click="test_name_and_data" type="primary" >上传</el-button>
          <el-button :style="{margin: '10px 50px'}">退出</el-button>

        </form-item>
      </i-form>
    </template>

  </div>
</template>


<style>

.DataUpload {

}


</style>


<script>
import axios from "axios";
import store from "../store/globalVar";
// import request from "@/request";
// var all_Cell_Data=0
// var name_list=0

// function requestConnection_getNameList() {
//   axios.get(this.$store.state.http_header + this.$store.state.ip + this.$store.state.connection_test)
//       .then(response => {
//         console.log(response);
//         getNameList()
//         getProcessedData()
//         // console.log(this.$store.state.b1c4)
//       })
//       .catch(function (error) {
//         console.log(error);
//       });
//   return 0
// }

// function getNameList() {
//   axios.get(this.$store.state.http_header + this.$store.state.ip + this.$store.state.route_name_list)
//       .then(response =>{
//         console.log(response);
//         name_list=response.data
//       })
//   return 0

// }

// function getProcessedData() {
//   axios.get(this.$store.state.http_header + this.$store.state.ip + this.$store.state.route_processed_data)
//       .then(response =>{
//         console.log(response);
//         all_Cell_Data=response.data
//       })
//   return 0
// }


export default {
  name: 'DataUpload',
  
  store,
  data() {
    return {
      formItem: {
        电池类型: '',
        select: '',
        radio: 'male',
        checkbox: [],
        switch: true,
        date: '',
        time: '',
        slider: [20, 50],
        textarea: '',

        border: 'NCA',



      },
      agingvalue: [0, 100],
      marks:{
        0:'SOH:0',
        20:'SOH:20',
        40:'SOH:40',
        60:'SOH:60',
        80:'SOH:80',
        100:'SOH:100',

      },
      cell_type_options: [{
        cell_type_value: '选项1',
        cell_type_label: '磷酸铁锂'
      }, {
        cell_type_value: '选项2',
        cell_type_label: '三元(NCA)'
      }, {
        cell_type_value: '选项3',
        cell_type_label: '三元(NCM)'
      }, {
        cell_type_value: '选项4',
        cell_type_label: '钛酸锂'
      }, {
        cell_type_value: '选项5',
        cell_type_label: '其他'
      }],
      cell_type_value: '',

      cell_warning_options: [{
        cell_warning_threshold_value: '选项1',
        cell_warning_threshold_label: '磷酸铁锂'
      }, {
        cell_warning_threshold_value: '选项2',
        cell_warning_threshold_label: '三元(NCA)'
      }, {
        cell_warning_threshold_value: '选项3',
        cell_warning_threshold_label: '三元(NCM)'
      }, {
        cell_warning_threshold_value: '选项4',
        cell_warning_threshold_label: '钛酸锂'
      }, {
        cell_warning_threshold_value: '选项5',
        cell_warning_threshold_label: '其他'
      }]
    }
  },

  mounted() {


  },

  methods: {
    requestConnection_getNameList(that) {
      axios.get(that.$store.state.http_header + that.$store.state.ip + that.$store.state.connection_test)
          .then(response => {
            console.log(response);
            that.$options.methods.getProcessedData(that)
            that.$options.methods.getNameList(that)
            
          })
          .catch(function (error) {
            alert(error)
            console.log(error);
          });
      return 0
    },

    getNameList(that) {
      axios.get(that.$store.state.http_header + that.$store.state.ip + that.$store.state.route_name_list)
          .then(response =>{
            console.log(response);
            that.$store.state.cell_name_list=response.data.name
          })
      return 0

    },

    getProcessedData(that) {
      axios.get(that.$store.state.http_header + that.$store.state.ip + that.$store.state.route_processed_data)
          .then(response =>{
            console.log(response);
            that.$store.state.all_cell_data=response.data.dependencies.all[0]
            // console.log(that.all_Cell_Data)
          })
      return 0
    },


    // open() {
    //   this.$alert('这是一段内容', '标题名称', {
    //     confirmButtonText: '确定',
    //     callback: action => {
    //       this.$message({
    //         type: 'info',
    //         message: `action: ${ action }`
    //       });
    //     }
    //   });
    // },


   /* *****************************************************/

    test_name_and_data(){
      const that=this
      // var all_Cell_Data = require('D:/DSC/硕士学习/课题组/前端/WebServer/Project/process_data/all_cell_data.json')
      // // var parameter = require('../../../../../../Project/process_data/parameter.json')
      // var name_list = require('D:/DSC/硕士学习/课题组/前端/WebServer/Project/process_data/nameList.json')

      // var all_Cell_Data = require('../../../../../../Project/process_data/all_cell_data.json')
      // // var parameter = require('../../../../../../Project/process_data/parameter.json')
      // var name_list = require('../../../../../../Project/process_data/nameList.json')

      this.$options.methods.requestConnection_getNameList(that)
      /*******************本地调试************************/
      // console.log(this.all_Cell_Data)
      // this.$store.state.all_cell_data = this.all_Cell_Data.dependencies.all[0]
      this.$store.state.b1c4 = this.$store.state.all_cell_data.b1c4
      // this.$store.state.b1c4_parameter = parameter
      console.log(null)
      console.log(this.$store.state.all_cell_data )
      console.log(this.$store.state.cell_name_list )
      // console.log(this.$store.state.b1c4_parameter )

      // this.$store.state.cell_name_list = this.name_list.name
      for (let cell in this.$store.state.all_cell_data){

        var currentcapacity = this.$store.state.all_cell_data[cell].capacity.capacity
        // console.log(currentcapacity)
        this.$store.state.current_capacity.push(currentcapacity[currentcapacity.length-1])

        this.$store.state.aging_degree.push((currentcapacity[0]-currentcapacity[currentcapacity.length-1])*100/currentcapacity[0])
      }


      // console.log(this.$store.state.current_capacity)
      // console.log( this.$store.state.aging_degree)



      this.$store.state.fig1_capacity = this.$store.state.all_cell_data.b1c4.capacity.capacity
      this.$store.state.fig1_cycle = this.$store.state.all_cell_data.b1c4.capacity.cycle
      // console.log( this.$store.state.fig1_cycle)
      // console.log( this.$store.state.fig1_capacity)
      this.$store.state.knee_point = this.$store.state.all_cell_data.b1c4.knee_point.knee_point

      this.$store.state.normalized_capacity = this.$store.state.all_cell_data.b1c4.knee_degree.normalized_capacity
      this.$store.state.normalized_cycle = this.$store.state.all_cell_data.b1c4.capacity.normalized_cycle

      this.$store.state.angle_degree = this.$store.state.all_cell_data.b1c4.online_degree_all.angle_degree
      this.$store.state.square_degree = this.$store.state.all_cell_data.b1c4.online_degree_all.square_degree

      // console.log( this.$store.state.angle_degree)
      // console.log( this.$store.state.square_degree)
      this.$store.state.online_rank = this.$store.state.all_cell_data.b1c4.online_rank_all.online_rank

      this.$store.state.predicted_ctk = this.$store.state.all_cell_data.b1c4.predicted_ctk.predicted_ctk
      this.$store.state.true_ctk = this.$store.state.all_cell_data.b1c4.predicted_ctk.true_ctk

      // this.$store.state.IC_DV = parameter.parameter.IC_DV
      // this.$store.state.IR = parameter.parameter.IR
      // this.$store.state.Qd_lin = parameter.parameter.Qd_lin
      // this.$store.state.V_lin = parameter.parameter.V_lin
      // this.$store.state.abs_IC_DV_max = parameter.parameter.abs_IC_DV_max
      // this.$store.state.abs_IC_DV_pos = parameter.parameter.abs_IC_DV_max_pos


      this.$confirm('是否确认上传?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'success',
          message: '上传成功!'
        });
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '上传失败'
        });
      });
    },


  },

  components: {},

  computed:{

  },

}

</script>
