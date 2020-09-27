<template lang="html">
  <div class="answer">
    <p>
      <span class="author">{{answer.author | capitalize}}</span>
      answered on {{answer.creationDate}}
    </p>
    <h6>{{answer.content}}</h6>
    <div v-if="isAnswerAuthor">
      <router-link class="btn btn-sm mr-2"
        :to="{name: 'AnswerEditor', params: {id: answer.id}}">
        <svg width="1em" height="1em" viewBox="0 0 16 16"
          class="bi bi-pencil-square" fill="currentColor"
          xmlns="http://www.w3.org/2000/svg">
          <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459
            3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75
            2.456l-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0
            .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
          <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5
            0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0
            1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1
            2.5v11z"/>
        </svg>
      </router-link>
      <button class="btn btn-sm ml-2" @click="triggerDelete">
        <svg width="1em" height="1em" viewBox="0 0 16 16"
          class="bi bi-trash-fill" fill="currentColor"
          xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1
            1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0
            0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1
            .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1
            .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5a.5.5 0 0 0-1 0v7a.5.5
            0 0 0 1 0v-7z"/>
        </svg>
      </button>
    </div>
    <div v-else>
      <button class="btn btn-sm" @click="toggleLike"
        :class="{'alreadyLiked': userLiked}">
        <svg width="1em" height="1em" viewBox="0 0 16 16"
          class="bi bi-hand-thumbs-up mr-2" fill="currentColor"
          xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M6.956 1.745C7.021.81 7.908.087
            8.864.325l.261.066c.463.116.874.456 1.012.965.22.816.533 2.511.062
            4.51a9.84 9.84 0 0 1 .443-.051c.713-.065 1.669-.072
            2.516.21.518.173.994.681 1.2 1.273.184.532.16 1.162-.234
            1.733.058.119.103.242.138.363.077.27.113.567.113.856 0
            .289-.036.586-.113.856-.039.135-.09.273-.16.404.169.387.107.819-.003
            1.148a3.163 3.163 0 0 1-.488.901c.054.152.076.312.076.465 0
            .305-.089.625-.253.912C13.1 15.522 12.437 16 11.5 16v-1c.563 0
            .901-.272 1.066-.56a.865.865 0 0 0
            .121-.416c0-.12-.035-.165-.04-.17l-.354-.354.353-.354c.202-.201.407-.511.505-.804.104-.312.043-.441-.005-.488l-.353-.354.353-.354c.043-.042.105-.14.154-.315.048-.167.075-.37.075-.581
            0-.211-.027-.414-.075-.581-.05-.174-.111-.273-.154-.315L12.793
            9l.353-.354c.353-.352.373-.713.267-1.02-.122-.35-.396-.593-.571-.652-.653-.217-1.447-.224-2.11-.164a8.907
            8.907 0 0 0-1.094.171l-.014.003-.003.001a.5.5 0 0 1-.595-.643 8.34
            8.34 0 0 0
            .145-4.726c-.03-.111-.128-.215-.288-.255l-.262-.065c-.306-.077-.642.156-.667.518-.075
            1.082-.239 2.15-.482 2.85-.174.502-.603 1.268-1.238
            1.977-.637.712-1.519 1.41-2.614
            1.708-.394.108-.62.396-.62.65v4.002c0 .26.22.515.553.55 1.293.137
            1.936.53 2.491.868l.04.025c.27.164.495.296.776.393.277.095.63.163
            1.14.163h3.5v1H8c-.605 0-1.07-.081-1.466-.218a4.82 4.82 0 0
            1-.97-.484l-.048-.03c-.504-.307-.999-.609-2.068-.722C2.682 14.464 2
            13.846 2 13V9c0-.85.685-1.432 1.357-1.615.849-.232 1.574-.787
            2.132-1.41.56-.627.914-1.28
            1.039-1.639.199-.575.356-1.539.428-2.59z"/>
        </svg>
        <strong>{{likesN}}</strong>
      </button>
    </div>
  </div>
</template>

<script>
  import {APIService} from "../common/API.service.js";
  export default {
    name: "AnswerComponent",
    props: {
      answer: {
        type: Object,
        required: true
      }, userName: {
        type: String,
        required: true
      }
    }, data() {return {
      userLiked: this.answer.hasVoted,
      likesN: this.answer.likes
    }}, computed: {isAnswerAuthor() {return this.answer.author === this.userName;}},
    methods: {
      triggerDelete() {this.$emit("deleteAnswer", this.answer);},
      toggleLike() {this.userLiked ? this.unlike() : this.like()},
      like() {
        this.userLiked = true;
        this.likesN += 1;
        let endpoint = `/API/answers/${this.answer.id}/like`;
        APIService(endpoint, "POST");
      }, unlike() {
        this.userLiked = false;
        this.likesN -= 1;
        let endpoint = `/API/answers/${this.answer.id}/like`;
        APIService(endpoint, "DELETE");
      }
    }
  }
</script>

<style lang="css" scoped>
  .answer {background-color: rgba(112, 128, 144, 0.1);
           margin: 2em 0;
           padding: 1em}
  .btn, .btn:link, .btn:active, .btn:visited {background-color: rgba(112, 128, 144, 0.25)}
  .btn:hover{background-color: var(--colour1);
             color: white}
  .alreadyLiked {background-color: var(--colour1);
                 color: white}
</style>
