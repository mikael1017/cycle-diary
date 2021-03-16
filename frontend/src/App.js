import Layout from "./hocs/Layout";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./containers/Home";
import About from "./containers/About";
import Signin from "./containers/Login";
import Signup from "./containers/Signup";
import notFound from "./components/Notfound";
import { Provider } from "react-redux";
import store from "./store";
import "./sass/main.scss";

const App = () => (
  <Provider store={store}>
    <Router>
      <Layout>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/about" component={About} />
          <Route exact path="/signin" component={Signin} />
          <Route exact path="/signup" component={Signup} />
          <Route component={notFound} />
        </Switch>
      </Layout>
    </Router>
  </Provider>
);

export default App;
