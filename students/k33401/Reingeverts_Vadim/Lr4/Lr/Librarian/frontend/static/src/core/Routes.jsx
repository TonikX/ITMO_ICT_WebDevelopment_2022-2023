import React from "react";
import { Switch, Route, Redirect } from "react-router";

import Library from "../components/Library";
import ROUTES from "constants/routes";

const Routes = () => {
    return (
        <>
            <Switch>
                <Route exact path="/">
                    <Redirect push to={ROUTES.LIBRARY} />
                </Route>
                <Route path={ROUTES.LIBRARY}>
                    <Library />
                </Route>
            </Switch>
        </>
    );
};

export default Routes;
