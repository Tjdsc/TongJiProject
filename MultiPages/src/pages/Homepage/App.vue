<template>
  <div id="app">
    <!--头部模块-->
    <web-top/>

    <!--轮播图模块-->
    <slide-show/>

    <!--智能电池解决方案模块-->
    <module-solution/>

    <!--新闻模块-->
    <news-box/>

    <!--网页尾部-->
    <footer-container/>
    
  </div>
</template>

<script>
import WebTop from '../../components/WebTop.vue'
import FooterContainer from '../../components/FooterContainer.vue'
import SlideShow from '../../components/SlideShow.vue'
import ModuleSolution from '../../components/ModuleSolution.vue'
import NewsBox from '../../components/NewsBox.vue'



export default {
  name: 'App',
  components: {
    WebTop,
    FooterContainer,
    SlideShow,
    ModuleSolution,
    NewsBox
    
  }
}
</script>

<style>
:root{
    --slideshow-text-color: #ffffff;
    --main_color:#F97F51;
}
</style>
