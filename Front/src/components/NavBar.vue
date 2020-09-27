<template lang="html">
  <nav class="navbar navbar-expand-lg">
    <router-link class="navbar-brand" :to="{name: 'Home'}">Questio</router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent" aria-expanded="false"
      aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ml-auto">
        <li class="nav-item">
          <router-link class="btn mr-5" :to="{name: 'QuestionEditor'}">
            Ask a question
          </router-link>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/accounts/logout/">Sign out</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
</script>

<style lang="css" scoped>
  nav {background-color: var(--colour1)}
  .navbar-brand, .nav-link {font-weight: bold;
                            color: white}
</style>
