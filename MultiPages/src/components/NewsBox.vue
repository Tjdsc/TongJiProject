<template>
  <div>
    <!--新闻模块-->
    <div class="news_total_title all_w">
        <h2 class="all_w">行业资讯</h2>
        <span class="divider_line all_w">——</span>
    </div>
    <!--可以上下滑动的盒子-->
    <div class="index_news all_w">
        <div class="news_card">
            <div class="news_img">
                <a href="#"><img src="../assets/news_img1.jpg" alt=""></a>
            </div>
            <div class="news_content">
                <h2 class="news_content_title">跟随《强国基石》，探秘长寿命电池的技术突破</h2>
                <p class="news_content_date">
                    2021-08-06
                </p>
            </div>
        </div>
        <div class="news_card">
            <div class="news_img">
                <a href="#"><img src="../assets/news_img2.jpg" alt=""></a>
            </div>
            <div class="news_content">
                <h2 class="news_content_title">宁德时代发布第一代钠离子电池</h2>
                <p class="news_content_date">
                    2021-07-29
                </p>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
/*首页新闻模块*/
.index_news{
    height: 450px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    /*padding: 10px;*/
}
.index_news .news_card{
    float: left;
    /*margin-top: 20px;*/
    position: relative;
    max-width: 460px;
    height: 215px;
    background: #fff;
    margin-right: 80px;
    padding: 20px 15px;
    display: flex;
    flex-direction: column;
    box-shadow: 0 5px 202px rgba(0,0,0,0.5);
    transition: .3s ease-in-out;
}
.index_news .news_card:hover{
    height: 300px;
}
.index_news .news_card .news_img{
    position: relative;
    width: 360px;
    height: 200px;
    top: -60px;
    margin-left: 20px;
    margin-right: 20px;
    z-index: 1;
    box-shadow: 0 5px 20px rgba(0,0,0,0.2);
}
.index_news .news_card .news_img img{
    width: 100%;
    height: 100%;
    border-radius: 4px;
}
.index_news .news_card .news_content{
    position: relative;
    margin-top: -140px;
    padding: 10px 15px;
    text-align: center;
    color: #111;
    visibility: hidden;
    opacity: 0;
    transition:all .3s ease-in-out;
}

.index_news .news_card:hover .news_content{
    visibility: visible;
    opacity: 1;
    margin-top: -40px;
    transition-delay:.3s;
}
.news_content .news_content_title{
    font-size: 18px;
}
.news_content .news_content_date{
    margin-top: 20px;
    font-size: 14px;
}

</style>