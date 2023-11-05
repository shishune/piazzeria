import "./PostEntry.css";
import { useState } from "react";

const title = "Q1.1";
const questionName = "Why is this website pizza themed?";
const studentAnswer = ":)";
const instructorAnswer = ":D";
const linkToQuestion = 1566;

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
        <strong>
          <i>Student's Answer: </i>
        </strong>
        {studentAnswer}
        <br />
        <strong>
          <i>Instructor's Answer: </i>
        </strong>
        {instructorAnswer}(
        <a
          target="_blank"
          rel="noreferrer"
          href={`https://piazza.com/class/jyumkm04gce137/post/${linkToQuestion}`}
        >
          @{linkToQuestion}
        </a>
        )
      </p>
    </div>
  );
}

export default PostEntry;
