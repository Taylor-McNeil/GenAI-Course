import { useParams } from "react-router-dom";

const WordDetail = () => {
  const { wordId } = useParams(); // Get word ID from URL

  return (
    <div>
      <h1>Word Details</h1>
      <p>Showing details for word ID: {wordId}</p>
    </div>
  );
};

export default WordDetail;
