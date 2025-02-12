import { useState } from "react";
import { getAllWords } from "../api"; // Import API function
import { Button } from "@/components/ui/button"


// ✅ WordList Component: Fetches and displays words
const WordList = () => {
  const [words, setWords] = useState<{ id: number; english_word: string; spanish_word: string;}[]>([]);

  // Function to fetch words
  const fetchWords = async () => {
    const data = await getAllWords();
    setWords(data);
  };

  return (
    <div>
      <h2>Word List</h2>
      <Button onClick={fetchWords}>Fetch Words</Button>
      <ul>
        {words.map((word) => (
          <li key={word.id}>
            {word.id} ({word.spanish_word}) - {word.english_word}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default WordList;
