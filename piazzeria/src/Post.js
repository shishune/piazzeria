import PostEntry from "./PostEntry";
import "./Post.css";

function Post({ isRAQOpen, setIsRAQOpen }) {
  return isRAQOpen ? (
    <div className="Post">
      <div className="PostBackground">
        <div className="CloseButtonContainer">
          <input
            type="image"
            className="CloseButton"
            src="xout.png"
            alt="Close Button. Fork and Knife on Plate"
            width="32"
            height="32"
            onClick={() => setIsRAQOpen(false)}
          />
        </div>
        <div className="PostBox">
          <PostEntry />
          <PostEntry />
        </div>
      </div>
    </div>
  ) : (
    <></>
  );
}

export default Post;
