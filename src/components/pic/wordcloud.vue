<template>
  <div class="cloud-wrap">     
    <!-- <dv-border-box-13> -->
    <h3>Top100-音乐词云
</h3> 
    <div class="cloud-box" ref="cloudEl" />
    <!-- </dv-border-box-13> -->
  </div>
</template>

<script>
import * as echarts from 'echarts'
import * as  wordcloud from "echarts-wordcloud";
export default {
  props: {},
  data() {
    return {
      wordcloud: wordcloud,
      cloudData: [
        {
    "name": "盛世美颜老妖蛾子",
    "value": "3736"
  },
  {
    "name": "Animenzzz",
    "value": "1963"
  },
  {
    "name": "TheMix多语种乐团",
    "value": "1501"
  },
  {
    "name": "音乐私藏馆",
    "value": "8627"
  },
  {
    "name": "绝对演绎",
    "value": "955"
  },
  {
    "name": "司墨尧smile",
    "value": "3288"
  },
  {
    "name": "面筋哥-程书林",
    "value": "941"
  },
  {
    "name": "典藏音悦",
    "value": "3006"
  },
  {
    "name": "肖恩Shaun-Gibson",
    "value": "962"
  },
  {
    "name": "共青团中央",
    "value": "729"
  },
  {
    "name": "音乐猛抬头",
    "value": "613"
  },
  {
    "name": "九三的耳朵不是特别好",
    "value": "742"
  },
  {
    "name": "TØm",
    "value": "3558"
  },
  {
    "name": "阿赫official",
    "value": "497"
  },
  {
    "name": "向晚大魔王",
    "value": "1570"
  },
  {
    "name": "翠花不太脆",
    "value": "728"
  },
  {
    "name": "勺Shaun",
    "value": "449"
  },
  {
    "name": "幸运的Muz",
    "value": "392"
  },
  {
    "name": "碰碰彭碰彭",
    "value": "1528"
  },
  {
    "name": "music你我他",
    "value": "66"
  },
  {
    "name": "豪灏號",
    "value": "482"
  },
  {
    "name": "不是柯桑德",
    "value": "8974"
  },
  {
    "name": "玩音乐的EZ",
    "value": "592"
  },
  {
    "name": "沧弦落尘",
    "value": "222"
  },
  {
    "name": "夏日入侵企画乐队",
    "value": "1212"
  },
  {
    "name": "周杰伦中文网JayCn",
    "value": "1688"
  },
  {
    "name": "大力滴滴滴",
    "value": "928"
  },
  {
    "name": "耳朵听了能怀孕",
    "value": "7015"
  },
  {
    "name": "暗杠",
    "value": "501"
  },
  {
    "name": "煮ル果実",
    "value": "473"
  },
  {
    "name": "Jason-老湿",
    "value": "2804"
  },
  {
    "name": "QQ音乐",
    "value": "4306"
  },
  {
    "name": "樱木君QAQ",
    "value": "6186"
  },
  {
    "name": "爱动手的小秦师傅",
    "value": "722"
  },
  {
    "name": "星辰_up",
    "value": "4988"
  },
  {
    "name": "醋醋cucu",
    "value": "457"
  },
  {
    "name": "胡侃音乐",
    "value": "4507"
  },
  {
    "name": "唯一8090",
    "value": "2461"
  },
  {
    "name": "张星特",
    "value": "1604"
  },
  {
    "name": "贾布加布",
    "value": "1824"
  },
  {
    "name": "哥谭噩梦赫然",
    "value": "851"
  },
  {
    "name": "黄龄",
    "value": "2671"
  },
  {
    "name": "GAI周延",
    "value": "519"
  },
  {
    "name": "LD的声乐游乐场",
    "value": "389"
  },
  {
    "name": "樱萍Apple",
    "value": "1568"
  },
  {
    "name": "音乐制作人Kurt",
    "value": "102"
  },
  {
    "name": "酷狗音乐",
    "value": "1780"
  },
  {
    "name": "aespa资源站",
    "value": "491"
  },
  {
    "name": "小王音乐馆",
    "value": "21"
  },
  {
    "name": "陆鳐LuLu",
    "value": "655"
  },
  {
    "name": "こはならむ",
    "value": "257"
  },
  {
    "name": "凤凰传奇",
    "value": "1271"
  },
  {
    "name": "天曰小雏Official",
    "value": "379"
  },
  {
    "name": "苍小天然呆bb",
    "value": "2936"
  },
  {
    "name": "蚕豆音乐娘",
    "value": "109"
  },
  {
    "name": "colorfulLifeTime",
    "value": "334"
  },
  {
    "name": "转世虚拟猫",
    "value": "293"
  },
  {
    "name": "一纸疯子",
    "value": "6"
  },
  {
    "name": "周深资讯站",
    "value": "3349"
  },
  {
    "name": "浑元Rysn",
    "value": "672"
  },
  {
    "name": "拯救世界的狗子",
    "value": "2589"
  },
  {
    "name": "妖精唱戏ing",
    "value": "565"
  },
  {
    "name": "ひとしずくP",
    "value": "427"
  },
  {
    "name": "丹哥的Sax",
    "value": "874"
  },
  {
    "name": "加油小仙",
    "value": "318"
  },
  {
    "name": "洛少爷",
    "value": "822"
  },
  {
    "name": "蜘蛛侠弹吉他",
    "value": "292"
  },
  {
    "name": "音乐老鸭煲",
    "value": "730"
  },
  {
    "name": "红豆_呀",
    "value": "12"
  },
  {
    "name": "阿拆家的昊然",
    "value": "3559"
  },
  {
    "name": "音樂魔法师",
    "value": "12"
  },
  {
    "name": "welater",
    "value": "1445"
  },
  {
    "name": "可人音乐",
    "value": "8"
  },
  {
    "name": "冰兔w",
    "value": "164"
  },
  {
    "name": "小美音乐",
    "value": "245"
  },
  {
    "name": "芝麻Mochi2",
    "value": "147"
  },
      ],
    };
  },
  mounted() {
    this.drawCloud(this.$refs.cloudEl, this.cloudData);
  },
  methods: {
    drawCloud(wrapEl, data) {
      let myChart = echarts.init(wrapEl);
      var option = {
        tooltip: {
          show: true,
        },
        series: [
          {
            name: "热词",
            type: "wordCloud",
            sizeRange: [10, 30],
            rotationRange: [-20, 20],
            shape: "circle",
            left: "center",
            top: "center",
            width: "100%",
            height: "80%",
            gridSize: 3,
            textPadding: 0,
            autoSize: {
              enable: true,
              minSize: 6,
            },
            textStyle: {
              normal: {
                color: function () {
                  return (
                    "rgb(" +
                    [
                      Math.round(Math.random() * 250),
                      Math.round(Math.random() * 250),
                      Math.round(Math.random() * 250),
                    ].join(",") +
                    ")"
                  );
                },
              },
              emphasis: {
                shadowBlur: 10,
                shadowColor: "#333",
              },
            },
            data: data,
            
          },
          console.log(data)
        ],
      };
      myChart.setOption(option);
    },
  },
};
</script>
<style lang="scss" scoped>
.cloud-wrap {
  width: 490px;
  height: 366px;
  text-align: left;
  .cloud-box {
    width: 100%;
    height: 100%;
  }
}
.dv-border-box-13{
    font-size: 10px;
    color: #fff;
    font-weight: bold;
    height: 100%;
}
h3{
  text-align: center;
}
</style>