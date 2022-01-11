<template>
  <div id="fors">
    <!-- <dv-border-box-8> -->
    <!-- 排名轮播表 -->
    
    <h4>全站排行榜Top100</h4>
      <dv-scroll-ranking-board :config="config" style="width:500px;height:500px" />
      <!-- </dv-border-box-8> -->
  </div>
</template>

<script>
export default {
    data() {
    return{
        config:{
        },
        };
        },
      created() {
      this.$nextTick(()=>{
        this.getall();
      });
    },
        methods: {
          async getall(){
            await this.axios
            .get('/get_all')
            .then((res)=>{
                this.config={
                  data:res.data,
                  rowNum:5,
                  waitTime:3000,
                  sort:false,
                }
                
                // console.log(res.data)

            })
            this.config={...this.config}
          }
        }

    
}
</script>

<style scoped>
#fors{
  height:470px!important;
  margin-left:20px;
}

</style>