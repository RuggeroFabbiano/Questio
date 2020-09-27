<template>
  <div v-if="questions.length>0" class="container mt-2">
    <div v-for="question in questions" :key="question.pk">
      <router-link :to="{name: 'Question', params: {slug: question.slug}}">
        <div class="question mt-3">
          <p>Question asked by
            <span class="author">{{question.author | capitalize}}</span>
          </p>
          <h5>{{question.content | questionize}}</h5>
          <p>Answers: {{question.nAnswers}}</p>
        </div>
      </router-link>
    </div>
    <div class="my-4">
      <p v-show="loadingQuestions">Loading more questions...</p>
      <button class="btn" v-show="next" @click="getQuestions">Show more questions</button>
    </div>
  </div>
  <div v-else class="mt-5">
    <h4>No questions yet. Be the first to ask one!</h4>
  </div>
</template>

<script>
  import {APIService} from "../common/API.service";
  export default {
    name: "home",
    data() {return {
      questions: [],
      next: null,
      loadingQuestions: false
    }},
    methods: {
      getQuestions() {
        let endpoint = "API/questions/";
        if (this.next) {endpoint = this.next;}
        this.loadingQuestions
        APIService(endpoint)
          .then(data => {
            this.questions.push(...data.results);
            this.loadingQuestions = false;
            if (data.next) {this.next = data.next;}
            else {this.next = null;}
          })
      }
    }, created() {
      this.getQuestions();
      document.title = "Questio";}
  };
</script>

<style lang="css" scoped>
  a:link, a:active, a:visited, a:hover {color: black;
                                        text-decoration: none}
  .question {background-color: rgba(192, 192, 192, 0.5);
             padding: 1em;
             border-radius: 25px}
  .question:hover {background-color: var(--colour2)}
  h4 {text-align: center}
  h5 {margin: 0.5em 0 0 0}
  p {margin:0; padding: 0}
</style>
