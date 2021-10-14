<template>
  <div id="app">
    <div id="navigation" style="min-width: 700px">
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" router>
        <el-menu-item index=""><i class="el-icon-upload el-icon--left"></i></el-menu-item>
        <el-menu-item index="/">首页</el-menu-item>

        <el-menu-item index="/DataUploadView" >文件上传</el-menu-item>
        <el-menu-item index="/DataProcessView">数据分析</el-menu-item>
        <el-menu-item index="/DataMonitorView">实时监测</el-menu-item>
        <el-submenu index="/DataMonitorView">
          <template slot="title">帮助</template>
          <el-menu-item index="4-1">选项1</el-menu-item>
          <el-menu-item index="4-2">选项2</el-menu-item>
          <el-menu-item index="4-3">选项3</el-menu-item>
          <el-submenu index="4-4">
            <template slot="title">选项4</template>
            <el-menu-item index="4-4-1">选项1</el-menu-item>
            <el-menu-item index="4-4-2">选项2</el-menu-item>
            <el-menu-item index="4-4-3">选项3</el-menu-item>
          </el-submenu>
        </el-submenu>
      </el-menu>

    </div>
    <div class="line"></div>
    <keep-alive>
      <router-view></router-view>
    </keep-alive>

  </div>
</template>

<style lang="less">
  #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  }
  .el-menu-demo{

  }
  #navigation{
  /*  margin-left: 60px;*/
  }


</style>

<script>
export default {
  data() {
    return {
      activeIndex: '1',
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>
