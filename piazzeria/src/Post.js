import PostEntry from "./PostEntry";
import "./Post.css";

function Post() {
  return (
    <div className="Post">
      <img className="PostBackground" src="box.png" alt="Open Pizza Box" />
      <div className="PostBox">
        <PostEntry />
      </div>
    </div>
  );
}

export default Post;
