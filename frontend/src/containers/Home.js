import React, { useState } from "react";
import { Helmet } from "react-helmet";
import Pagination from "../components/Pagination";
import Trips from "../components/Trips";

const home = () => {
  const [diaries, setDiaries] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [diariesPerPage, setDiariesPerPage] = useState(3);
  const [active, setActive] = useState(1);

  const indexOfLastDiary = currentPage * diariesPerPage;
  const indexOfFirstDiary = indexOfLastDiary - diariesPerPage;
  const currentDiary = diaries.slice(indexOfFirstDiary, indexOfLastDiary);

  const visitPage = (page) => {
    setCurrentPage(page);
    setActive(page);
  };

  const previous_number = () => {
    if (currentPage !== 1) {
      setCurrentPage(currentPage - 1);
      setActive(currentPage - 1);
    }
  };

  const next_number = () => {
    if (currentPage !== Math.cell(diaries.length / 3)) {
      setCurrentPage(currentPage + 1);
      setActive(currentPage + 1);
    }
  };

  return (
    <main className="home">
      <Helmet>
        <title> Cycle Diary - Home</title>
        <meta name="description" content="Cycle Diary Home Page" />
      </Helmet>
      <section className="home__form"></section>
    </main>
  );
};

export default home;
