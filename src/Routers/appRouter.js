import React from 'react'
import {Router, Switch, Route} from 'react-router'
import {createBrowserHistory} from 'history'
import Error from '../components/Error'
import ViewBooks from '../components/ViewBooks'
import ViewMembers from '../components/ViewMembers'
import ViewTransactions from '../components/ViewTransaction'
import Transaction from '../components/Transaction'
const history = createBrowserHistory()
export default ()=>(
    <Router history={history}>
        <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="/">Library</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/Books">Books</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/Members">Members</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"></input>
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
            <Switch>
                <Route path='/' component={ViewTransactions} exact={true}/>
                <Route path='/transaction:id' component={Transaction}/>
                <Route path='/Books' component={ViewBooks}/>
                <Route path='/Members' component={ViewMembers}/>
                <Route component={Error}/>
            </Switch>
        </div>
    </Router>
)