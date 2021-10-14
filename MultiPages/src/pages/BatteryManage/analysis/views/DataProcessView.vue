<template>
  <div class="layout">
    <Layout>
      <Layout :style="{padding: '0 50px'}">
        <Breadcrumb :style="{margin: '16px 0',minWidth:'500px'}">
          <BreadcrumbItem>Home</BreadcrumbItem>
          <BreadcrumbItem>Components</BreadcrumbItem>
          <BreadcrumbItem>Layout</BreadcrumbItem>
        </Breadcrumb>
        <Content :style="{padding: '24px 1', minHeight: '280px', background: '#fff', width: '1200px'}">
          <Layout>
            <Sider hide-trigger :style="{background: '#fff'}">
              <Menu active-name="1-1" theme="light" width="auto" :open-names="['1']">

                <Submenu id="all_cells" name="1">
                  <template slot="title">
                    <Icon type="ios-analytics"></Icon>
                    所有电池
                  </template>
                  <MenuItem name="1-1" @click.native="all_cell_data">容量曲线</MenuItem>
                  <MenuItem name="1-2">老化分布</MenuItem>

                </Submenu>
                <Submenu id="cell-list-1" name="2" >
                  <template slot="title">
                    <Icon type="ios-navigate"></Icon>
                    电池单体
                  </template>
                  <div v-for="(item,key) in nameList" :key="key" >
                    <MenuItem  :name="2-key" @click.native="single_Cell_Data(item)">{{ item }}</MenuItem>
                  </div>
                </Submenu>
                <Submenu id="cell-list-2" name="3">
                  <template slot="title">
                    <Icon type="ios-keypad"></Icon>
                    灵活对比
                  </template>
                  <MenuItem name="3-1">Option 1</MenuItem>
                  <MenuItem name="3-2">Option 2</MenuItem>
                </Submenu>

              </Menu>
            </Sider>
            <Content :style="{padding: '24px 80px 24px 80px', minHeight: '280px', background: '#fff', width: '850px',margin:'0 0px 0 0px'}">
              <template>

                <div v-if="pageType == 'single_cell'">
                  <com-single-cell :item="item"></com-single-cell>
                </div>

                <div v-if="pageType == 'all_cell'">
                  <com-all-cell ></com-all-cell>
                </div>


              </template>

            </Content>
          </Layout>
        </Content>
      </Layout>
      <Footer class="layout-footer-center">2011-2016 &copy; TalkingData</Footer>
    </Layout>
  </div>
</template>

<script type="text/javascript">


import store from '../store/globalVar'
import comsinglecell from '../component/singleCell'
import allcell from '../component/allCell'


export default {
name: "DataProcess",

  data(){
    return{

      pageType:null,
      item:'',

    }
  },
  components:{
    'com-single-cell':comsinglecell,
    'com-all-cell':allcell
  },

  store,
  mounted(){
  },

  created() {

  this.item = 'cccc'
  },

  methods:{
    single_Cell_Data(item) {
      this.pageType = 'single_cell'
      console.log(this.pageType);
      this.item = item
      this.$store.state.current_cell_name = item
      // console.log(this.$store.state.current_cell_name)

    },

    all_cell_data(){
      this.pageType = 'all_cell'
      this.item = 'all_capacity'
    },
  },

  computed:{
      nameList(){
        return this.$store.state.cell_name_list
      },


  },

}

</script>

<style scoped>



.layout{
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
}

.layout-footer-center{
  text-align: center;
}


</style>
