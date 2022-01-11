<template>
  <!-- <Resize >
   
  </Resize> -->
   <Topbilibili/>
</template>

<script>
import Topbilibili from './components/Topbilibili.vue'
// import Resize from './components/util/Resize.vue'
export default {
  name: 'App',
  components: {
    Topbilibili,
    // Resize,
  }
}
</script>

<style>
body{
  margin:0
  
}
body,html{
    width:100%;
  height:100%;
}
#resize,#app{
  width:100%!important;
  height:100%!important;
}
</style>
