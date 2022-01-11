<template>
  <div class="cc-details">   
      <div class="card">B</div>
      <div class="card">站</div>
      <div class="card">大</div>
      <div class="card">屏</div>
      <div class="card">可</div>
      <div class="card">视</div>
      <div class="card">化</div>
    </div>

</template>

<script>
export default {

}
</script>

<style>
.cc-details {
  float: right;
    height: 120px!important;
    display: flex;
    justify-content: flex-start;
    font-size: 32px;
    align-items: center;
    flex-direction: column;
    flex-wrap: wrap;
    
  }
  .cc-details,.card {
      width: 70px;
      color: #08e5ff;
      font-weight: bold;
      line-height: 35px;
      text-align: center;
      margin: 10px;
      align-content: flex-end;
      flex-shrink:1;
    }
.card {
      background-color: rgba(4,49,128,.6);
      height: 40px;
      
      font-size: 35px;
    }
</style>