import WordList from "../components/WordList"; // Import the WordList component

const Words = () => {
  return (
    <div>
      <h1>This is the future words list page</h1>
      <WordList /> {/* Reuse the word list component */}
    </div>
  );
};

export default Words;