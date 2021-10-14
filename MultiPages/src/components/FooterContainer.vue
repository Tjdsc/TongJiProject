<template>
  <div class="footer_container">
    <div class="container_box">
        <div class="footer_logo">
            <img src="../assets/logo.png" alt="logo">
            <p class="footer_faith">智慧电池致力于提供关于智能管理电池的最优算法</p>
        </div>
        <div class="footer_links">
            <dl>
                <dt>关于我们</dt>
                <dd><a href="public/index.html">公司简介</a></dd>
                <dd><a href="public/news.html">新闻快讯</a></dd>
                <dd><a href="public/about.html">加入我们</a></dd>
            </dl>
            <dl>
                <dt>智能解决方案</dt>
                <dd><a href="public/batterymanage.html">实时观测电池老化</a></dd>
                <dd><a href="public/batterymanage.html">容量“跳水”多级预警</a></dd>
                <dd><a href="public/batterymanage.html">快速充电</a></dd>
            </dl>
            <dl class="footer_contact">
                <dt>联系我们</dt>
                <dd><span class="iconfont icon-address"></span>地址：上海市嘉定区</dd>
                <dd><span class="iconfont icon-phone"></span>电话：18XXXXXXXXX</dd>
                <dd><span class="iconfont icon-mail"></span>邮箱：xxxx@xxx.com</dd>
            </dl>
        </div>
        <div class="copyright_text">
            Copyright©2020-2021上海智慧电池科技有限责任公司 沪ICP备20009695号
        </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
/*网页尾部-start*/
.footer_container{

    width: 100%;
    height: 300px;
    background-color: var(--header-background-color);
}
.container_box{
    width: 100%;
    height: 100%;
    position: relative;
    animation: focus-in-expand-fwd 0.8s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
}
.footer_logo{
    float: left;
    height: 100%;
    width: 500px;
    /*margin: 50px 80px;*/
    text-align: center;
}
.footer_logo img{
    margin-top: 50px;
    width: 200px;
    height: 80px;
}
.footer_faith{
    margin-top: 20px;
    font-size: 12px;
    color: var(--slideshow-text-color);
}
.footer_links{
    float: left;
    margin-top: 50px;
}
.footer_links dl{
    float: left;
    margin-right: 80px;
}
.footer_links dt{
    /*color: #646464;*/
    font-size: 18px;
    margin-bottom: 10px;
}
.footer_links dd{
    /*color: var(--slideshow-text-color);*/
    font-size: 16px;
    line-height: 2em;
}
.footer_links .footer_contact dd{
    font-size: 20px;
    color: var(--slideshow-text-color);
}
.footer_links .footer_contact span{
    font-size: 24px;
    color: var(--slideshow-text-color);
    margin-right: 5px;
}
.copyright_text{
    position: absolute;
    bottom: 10px;
    font-size: 14px;
    color: var(--slideshow-text-color);
    left: 50%;
    transform: translateX(-50%);
}

@keyframes focus-in-expand-fwd {
    0% {
        letter-spacing: -0.5em;
        transform: translateZ(-800px);
        filter: blur(12px);
        opacity: 0;
    }
    100% {
        transform: translateZ(0);
        filter: blur(0);
        opacity: 1;
    }
}
/*尾部-end*/
</style>