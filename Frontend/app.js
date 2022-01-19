const routes=[
    {path:'/home',component:home},
    {path:'/user',component:user},
    {path:'/blahaj',component:blahaj}
]

const router=new VueRouter({
    routes
})

const app = new Vue({
    router
}).$mount('#app')