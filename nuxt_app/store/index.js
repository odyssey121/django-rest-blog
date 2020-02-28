
export const actions = {
    getPosts(vuexContext, context) {
        return this.$axios.$get("api/articles/")
            .then(res => {
                console.log(res)
                let postArr = [];
                for (let key in res) {
                    postArr.push({ ...res[key], id: key })
                }
                vuexContext.commit('SET_POSTS', postArr)
            })
            .catch(err => console.log(err))
    }
}

export const mutations = {
    SET_POSTS(state, posts) {
        state.posts = posts
    },
    CREATE_POST(state, post) {
        state.posts.push(post)
    },
    EDIT_POST(state, post) {
        let index = state.posts.findIndex(record => record.id === post.id)
        if (index >= 0) {
            state.posts[index] = { ...post }
        }


    }
}

export const getters = {
    getPosts: (state, _getters) =>
        state.posts
    ,
    getPostById: (state, _getters) => id =>
        state.posts.filter(record => record.id === id).pop()
}

export const state = () => ({ posts: [] })