<template>
  <div id="right_chart1">
    <h4>游戏Top100-播放量</h4>
    <dv-scroll-board :config="config" style="width: 500px; height: 50px" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      config: {        
      },
    };
  },
  created() {
    this.$nextTick(() => {
      this.getgameplay();
    });
  },
  mounted() {
    // this.getgameplay();
  },
  methods: {
    async getgameplay() {
      await this.axios
      .get("/get_game_play")
      .then(res =>{
        // console.log(res.data)
        this.config={
              // header:['up','play'],
              data:res.data,
              rowNum:1,
              align:['center'],
              headerHeight:10,
              index:true,
        }
        // console.log(res.data)
        
      }) 
      this.config = { ...this.config }
    },
  },
};
</script>

<style>
.right_chart1{
  position:relative;
  z-index:999;
}
</style>