# Cookiecutter Vue3 + Vite + Django

[![Build Status](https://img.shields.io/github/actions/workflow/status/ilikerobots/cookiecutter-django/ci.yml?branch=vue3-vite)](https://github.com/ilikerobots/cookiecutter-django/actions/workflows/ci.yml?query=branch%3Avue3-vite)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


Vue 3 (Vite) Cookiecutter Django jumpstarts a production-ready, developer-friendly Django + Vue project quickly.
Have the best of both front-ends by mounting Vue components directly into Django Templates.

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter).

***Note***: *There is also an older, outdated [Webpack version of this cookiecutter](https://github.com/ilikerobots/cookiecutter-vue-django/tree/master).*

## Features

- Harmonious integration of Django Templates and Vue 3 
- Vue Single File Components (SFCs)
- Vite-based build
- Lightning fast Hot Module Replacement (HMR) for Vue components
- Pinia state management, shared among any components on the same template
- Persistent state across page loads
- Pass data from Django to Vue 
  - Property passing from Template -> Root Vue Component
  - Provide/Inject from Template -> Vue
  - "Django Slots" to pass arbitrary HTML to Vue components
- Vue devtools support
- Sass/SCSS pre-compilation of Vue Components
- Chunked resource loading 
- Teleport Vue components across Django templates
- All the features of the amazing [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django)


## Usage

First, get Cookiecutter. Trust me, it's awesome:

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo:

    $ cookiecutter https://github.com/ilikerobots/cookiecutter-vue-django

You'll be prompted for some values. Provide them, then a Django project will be created for you.

For more instructions, see [upstream cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django)

## Running the Vite Dev server

#### With Docker

If you have enabled docker in your cookiecutter configuration, then the Vite dev server will automatically run with the
local configuration:

```
docker compose -f local.yml build
docker compose -f local.yml up
```

If for any reason you wish to build a static build on the local docker configuration, you may run:
`docker-compose -f local.yml run vite vite build`

#### With PyCharm

The Vite dev server may be run from PyCharm using the pre-built run configurations.  First, ensure that 
PyCharm project's Node interpreter is properly set (Languages & Frameworks -> Node.js), then run the run 
configuration named ```npm install```.  After that, run the configuration named `vite dev` to launch Vite dev server.


#### From the console
From your project directory:

```sh
cd vue_frontend
npm install
npm run dev
```

## Static Vite Builds

For production deployment, the Vue frontend must be built into static resources, which will be served
using the same Django staticfiles strategy as the rest of your site.  If using docker, this step is included
in the production configuration.  If not using Docker, then you must include the Vite build step into your 
build/deploy process (see below).  Note this must be done before the `collectstatic` management task is run.

The setting `VUE_FRONTEND_USE_DEV_SERVER` dictates whether your Django app will be expecting to serve Vue assets from
the Vite Dev Server or from a static build.  This setting defaults to the same as `DEBUG`.

#### With Docker

The production docker configuration includes the Vite build step automatically when the images are built.


#### With Pycharm

Assuming you have enabled pycharm support, then simply run the `vite build` run configuration.

#### From the console

From the `vue_frontend` directory: 
```sh
npm run build
```

