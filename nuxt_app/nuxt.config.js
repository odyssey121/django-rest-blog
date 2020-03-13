var stylus = require("stylus");
var path = require("path");
function p() {
  return path.resolve(__dirname, ...arguments);
}
export default {
  mode: "spa",

  /*
   ** Headers of the page
   */
  head: {
    title: process.env.npm_package_name || "",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "description",
        name: "description",
        content: process.env.npm_package_description || ""
      }
    ],
    link: [
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/icon?family=Material+Icons"
      },
      { rel: "icon", type: "image/x-icon", href: "/favicon.ico" }
    ]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: false,

  /*
   ** Global CSS
   */
  css: ["assets/style/main.css"],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: ["~plugins/ui-component.js"],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [],
  /*
   ** Nuxt.js modules
   */
  modules: [
    "@nuxtjs/axios",
    "nuxt-quasar",
    ["@nuxtjs/proxy", { pathRewrite: { "^/api": "/api" } }]
  ],
  axios: {
    // baseURL: process.env.BASE_URL || 'http://127.0.0.1:8000/',
    // credentials: false
  },
  quasar: {
    // animations: ["fadeIn", "fadeOut"],
    framework: {
      iconSet: "fontawesome-v5",
      // config: {
      //   brand: {
      //     primary: "#ffffff",
      //     // ...
      //   },
      // },
      components: [
        "QList",
        "QItem",
        "QItemSection",
        "QItemLabel",
        "QChip",
        "QTabs",
        "QTab",
        "QRouteTab",
        "QForm",
        "QInput",
        "QToggle",
        "QIcon",
        "QBtn",
        "QBtnToggle"
      ],
      // directives: ["ClosePopup"],
      // plugins: ["Cookies"],
      // iconSet: "fontawesome-v5",
      cssAddon: true
    },
    supportIE: true,
    htmlVariables: {}
  },
  transition: {
    name: "fade",
    mode: "out-in"
  },

  proxy: {
    "/api": "http://127.0.0.1:8000/"
  },
  /*
   ** Build configuration
   */
  build: {}
};
