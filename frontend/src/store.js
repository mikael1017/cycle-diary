import { createStore, applyMiddleware } from "redux";
import { composeWithDevTools } from "redux-devtools=extension";
import thunk from "redux-thunk";
import rootReducers from "./reducers";

const initialState = {};

const middleware = [thunk];

const store = createStore(
  rootReducer,
  initialState,
  composeWithDevTools(appplyMiddleware(...middleware))
);

export default store;
