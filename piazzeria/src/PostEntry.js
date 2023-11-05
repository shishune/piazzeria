import "./PostEntry.css";
import { useState } from "react";

const title = "Q1.1";
const questionName = "Why is this website pizza themed?";
const studentAnswer = ":)";
const instructorAnswer = ":D";
const linkToQuestion = "";

function PostEntry() {
  const [isOpen, setIsOpen] = useState(true);

  return isOpen ? (
    <div
      className="PostEntryOpen"
      onClick={() => {
        setIsOpen(!isOpen);
      }}
    >
      <div className="PizzaSliceContainer">
        <img
          className="PizzaSlice"
          src="slice.png"
          alt="A Single Pizza Slice Facing East"
        />
      </div>
      <p className="Question">
        <strong>{title}</strong> <br />
        {questionName}
      </p>
    </div>
  ) : (
    <div
      className="PostEntryClose"
      onClick={() => {
        setIsOpen(!isOpen);
      }}
    >
      <div className="QuestionContainer">
        <div className="PizzaSliceContainer">
          <img
            className="PizzaSlice"
            src="slice.png"
            alt="A Single Pizza Slice Tilted Down"
          />
        </div>
        <p className="Question">
          <strong>{title}</strong> <br />
          {questionName}
        </p>
      </div>
      <p className="AnswerContainer">
        {studentAnswer}
        <br />
        {instructorAnswer}
        {linkToQuestion}
      </p>
    </div>
  );
}

export default PostEntry;
