<template>
  <div id="app">
    <!--头部模块-->
    <web-top/>

    <!--网页尾部-->
    <footer-container/>
    
  </div>
</template>

<script>
import WebTop from '../../components/WebTop.vue'
import FooterContainer from '../../components/FooterContainer.vue'


export default {
  name: 'App',
  components: {
    WebTop,
    FooterContainer
    
  }
}
</script>

<style>

</style>
