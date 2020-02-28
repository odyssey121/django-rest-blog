<template>
  <div class="post-item shadow-5">
    <div class="post-header flex-between">
      <div class="post-title">{{post.title}}</div>
      <div class="date">February 21 2020</div>
    </div>
    <div class="posted">
      Posted by:
      <q-chip dense color="orange" text-color="white" style="margin:0 1rem;">
        <a href="#">{{post.author}}</a>
      </q-chip>
      under
      <ul>
        <li v-for="(category, index) in post.categories" :key="index">
          <q-chip dense color="primary" text-color="white">
            <a href="#">{{ category }}</a>
          </q-chip>
          <span v-if="index < post.categories.length - 1">,</span>
          <span v-else>.</span>
        </li>
      </ul>
    </div>
    <div class="post-body">
      <p>{{post.body}}</p>
      <div
        class="thumbnail"
        style="background-image :url(https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTPIQC47XkB4VwelYMfc1G-T4uLnhNGz5er7xveCj0hiWgAu3Yg)"
      ></div>
    </div>
    <div class="post-footer flex-between">
      <a href="#">Read More...</a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    post: {
      type: Object,
      required: true
    }
  },
  data() {
    return {};
  }
};
</script>

<style lang="scss" scoped>
.flex-between {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.post-item {
  margin: 1rem 0;
  padding: 1rem;
  #author-sp {
    margin: 0 0.5rem;
  }
  .posted {
    border-bottom: 1px solid #ccc;
    display: flex;
    align-items: center;
    margin-bottom: 16px;
    ul {
      margin: 0 0 0 1rem;
      li {
        display: inline-block;
        a {
          color: inherit;
        }
      }
    }
  }
  .post-body {
    display: flex;
    justify-content: space-between;
    width: 100%;
    p {
      font-size: 120%;
      line-height: 150%;
    }
    .thumbnail {
      min-height: 120px;
      width: 200px;
      background-position: center;
      background-size: cover;
      margin-bottom: 16px;
    }
  }
}

.date {
  padding: 2px 8px;
  border: 1px solid #ccc;
  color: #666;
}
</style>
