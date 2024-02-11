import AuthorHome from "./components/authorhome.js";
import BlogHome from "./components/bloghome.js";

const routes = [
    {
        path: "/",
        component: AuthorHome,
        name: "Author home"
    },
    {
        path: "/blog",
        component: BlogHome,
        name: "Blog home"
    }
];


const router = new VueRouter({
    routes
});

export default router;