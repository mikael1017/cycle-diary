import React from "react";

const about = () => {
  return (
    <div className="auth">
      <Helmet>
        <title>Cycle Diary - About</title>
        <meta name="description" content="about page" />
      </Helmet>
      <h1 className="about__title"> About Jaewoo</h1>
      <p className="about__lead">This is Jaewoo's cycle diary</p>
    </div>
  );
};
export default about;
