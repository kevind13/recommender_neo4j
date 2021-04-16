# A simple and good recommender using Neo4j as DB 🔍

## First steps

Install all dependencies in the project directory with the command:

### `npm install`

Go to the `API` folder which contains the backend and create a new python enviroment then run:

### `[sudo] pip install -r requirements.txt`

You must have Neo4j installed and run it on your machine, create a database and fill it with the instructions found in `\api\cypher_commands.txt`

## Running

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

Also run:

### `yarn start-api`

Runs the api in Flask in the development mode.\
Open [http://localhost:5000](http://localhost:5000) to view it in the browser.

This depend on your machine, sometimes you have to change the way it is executed in the `package.json` file by modifying the direction of the Script.
or just go to API directory and run `python app.py`

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
