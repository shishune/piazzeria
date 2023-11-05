import PostEntry from "./PostEntry";
import "./Post.css";

function Post() {
  return (
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
          />
        </div>
        <div className="PostBox">
          <PostEntry />
          <PostEntry />
        </div>
      </div>
    </div>
  );
}

export default Post;
