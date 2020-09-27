{% load static%}
<template lang="html">
  <div class="mt-5">
    <img src="../../../Static/404.svg" alt="error 404">
    <h4>{{message}}</h4>
  </div>
</template>

<script>
  export default {
    name: "NotFound",
    data() {return {
      message: "Oups, it seems we cannot find the resource you're looking for"
    }}
  }
</script>

<style lang="css" scoped>
  .mt-5 {text-align: center}
  img {width: 50%}
  h4 {margin-top: -120px; font-weight: bold}
</style>
