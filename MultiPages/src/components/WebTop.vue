<template>
  <div class="web_top_bg">
    <div class="web_top_content">
    <!--头部logo-->
        <div class="logo">
            <img src="../assets/logo.png" alt="公司Logo">
        </div>
    <!--头部搜索框-->
        <div class="search-box">
            <input class="search-txt" type="text" placeholder="动态搜索框">
            <a class="search-btn">
                <svg class="icon" viewBox="0 0 1024 1024" width="30px"><path d="M424.024 766.098c-91.619 0-177.754-35.679-242.538-100.464-133.735-133.737-133.735-351.344 0-485.078 64.784-64.784 150.919-100.462 242.538-100.462s177.754 35.677 242.539 100.462c133.733 133.735 133.735 351.34 0 485.078-64.785 64.783-150.922 100.464-242.539 100.464zM424.024 196.085c-60.637 0-117.643 23.613-160.523 66.489-88.512 88.51-88.51 232.53 0 321.040 42.876 42.876 99.885 66.491 160.523 66.491s117.643-23.614 160.523-66.491c88.51-88.51 88.51-232.53 0-321.040-42.876-42.876-99.885-66.489-160.523-66.489z" fill="#e94118" p-id="1176"></path><path d="M886.838 943.904c-14.842 0-29.684-5.663-41.010-16.986l-261.286-261.285c-22.647-22.649-22.647-59.369 0-82.018 22.647-22.647 59.37-22.647 82.018 0l261.286 261.286c22.647 22.649 22.647 59.369 0 82.018-11.325 11.322-26.167 16.985-41.010 16.985z" fill="#e94118" p-id="1177"></path></svg>
            </a>
        </div>
    <!--头部导航栏-->
        <div class="nav_container">
            <ul>
                <li>
                    <a href="index.html">首页</a>
                </li>
                <li>
                    <a href="batterymanage.html">电池管理</a>
                    <ol>
                        <li><a href="batterymanage.html">电池全面分析</a></li>
                        <li><a href="batterymanage.html">超级快充</a></li>
                    </ol>
                </li>
                <li>
                    <a href="casecentre.html">案例中心</a>
                </li>
                <li>
                    <a href="news.html">新闻</a>
                </li>
                <li>
                    <a href="about.html">关于我们</a>
                    <ol>
                        <li><a href="about.html">公司简介</a></li>
                        <li><a href="about.html">联系我们</a></li>
                    </ol>
                </li>
                <li class="background_move start_home"></li>
            </ul>
        </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
/*头部背景*/
.web_top_bg{
    height: 85px;
    background-color: var(--header-background-color);
    z-index: -2;
}
/*头部大盒子*/
.web_top_content{
    width: 1200px;
    margin: 0 auto;
}
.logo{
    float: left;
    margin: 2px 10px 2px 5px;
}
.logo img{
    height: 80px;
    width: 220px;
}
/*动态搜索框模块-start*/
.search-box{
    float: left;
    background: var(--search-background-color);
    height: 60px;
    border-radius: 60px;
    /*padding: 10px;*/
    margin: 10px 20px 10px 50px;
    display: flex;
    justify-content: center;
}
.search-box:hover>.search-txt{
    width: 280px;
    padding: 0 6px;
}
.search-box:hover>.search-btn{
    background: white;
}
.search-btn{
    float: right;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: var(--search-background-color);
    display: flex;
    justify-content: center;
    align-items: center;
    transition: 0.4s;
    cursor: pointer;
}
.search-txt{
    border: none;
    background: none;
    outline: none;
    float: left;
    padding: 0;
    color: #ffffff;
    font-size: 16px;
    transition: 0.4s;
    line-height: 60px;
    width: 0;
}
/*动态搜索框模块-end*/
/*头部导航栏_start*/
.nav_container{
    /*position: relative;*/
    float: right;
    height: 100%;
    background-color: var(--search-background-color);
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}
.nav_container ul{
    display: flex;
    /*justify-content: space-around;*/
    position: relative;
    height: 100%;
}
.nav_container ul > li{
    /*float: left;*/
    height: 85px;
}
.nav_container ul > li > a{
    position: relative;
    /*float: left;*/
    display: block;
    width: 100%;
    height: 100%;
    z-index: 10;
    line-height: 85px;
    font-size: 16px;
    font-weight: bold;
    padding: 0 20px 0 20px;
    color: #ffffff;
}
.nav_container ul > li ol{
    position: relative;
    width: 100%;
    background-color: var(--navigation_background-color);
    border-radius: 8px;
    box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    /* 让盒子先沿着y轴缩放到0 也就是隐藏了 */
    transform: scaleY(0);
    /* 我们需要将盒子从上面滑动下来 设置一下缩放的中心点即可 设置到最上面的中间位置 */
    transform-origin: 50% 0;
    /* 设置过渡 */
    transition: all 0.5s;
    z-index: 999;
    /*使用z-index该元素必须为除static以外的定位*/
}
.nav_container ul > li ol li{
    height: 70px;
    border-radius: 8px;
}
.nav_container ul > li ol li a{
    display: block;
    color: var(--slideshow-text-color);
    font-size: 14px;
    width: 100%;
    height: 100%;
    line-height: 70px;
    text-align: center;
}
.nav_container ul > li ol li:hover{
    background-color: var(--navigation_background-color);
}
.nav_container ul > li:hover ol{
    transform: scaleY(1);
}
.nav_container ul .background_move {
    position: absolute;
    left: 0;
    top: 0;
    width: 76px;
    height: 100%;
    background-color: var(--navigation_background-color);
    z-index: 9;
    border-radius: 8px;
    transition: all .3s;
}
.start-home,
.nav_container ul > li:nth-child(1):hover~.background_move {
    width: 72px;
    left : 0;
}
.start-management,
.nav_container ul > li:nth-child(2):hover~.background_move {
    width: 104px;
    left : 72px;
}
.start-example,
.nav_container ul > li:nth-child(3):hover~.background_move {
    width: 104px;
    left : 176px;
}
.start-news,
.nav_container ul > li:nth-child(4):hover~.background_move {
    width: 72px;
    left : 280px;
}
.start-about,
.nav_container ul > li:nth-child(5):hover~.background_move {
    width: 104px;
    left : 352px;
}
/*头部导航栏-end*/
</style>